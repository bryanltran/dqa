import librosa
import tensorflow as tf
import numpy as np
from collections import Counter

SAVED_MODEL_PATH = "models/model.keras"
SAMPLES_TO_CONSIDER = 22050  # ~1 second of audio at 22050Hz

class KeywordSpottingService:
    """Singleton class for keyword spotting inference with trained models.
    Handles audio files of any length by processing them in chunks.
    """
    model = None
    _mapping = [
        "no", "yes"
    ]
    _instance = None

    def predict(self, file_path, confidence_threshold=0.5, min_detections=2):
        """
        Predict keywords in an audio file of any length.
        
        Args:
            file_path (str): Path to audio file
            confidence_threshold (float): Minimum confidence score to consider a detection valid
            min_detections (int): Minimum number of detections needed to report a keyword
        
        Returns:
            list: List of tuples containing (keyword, start_time, end_time, confidence)
        """
        # Load and process audio in chunks
        chunks_mfcc = self._process_audio_chunks(file_path)
        
        # Make predictions for each chunk
        predictions = []
        for i, mfcc_chunk in enumerate(chunks_mfcc):
            # Prepare the chunk for prediction
            mfcc_chunk = mfcc_chunk[np.newaxis, ..., np.newaxis]
            
            # Get prediction probabilities
            pred_probs = self.model.predict(mfcc_chunk, verbose=0)[0]
            pred_idx = np.argmax(pred_probs)
            confidence = pred_probs[pred_idx]
            
            # Only keep predictions above confidence threshold
            if confidence >= confidence_threshold:
                keyword = self._mapping[pred_idx]
                start_time = i * (SAMPLES_TO_CONSIDER / 22050)  # Convert to seconds
                end_time = (i + 1) * (SAMPLES_TO_CONSIDER / 22050)
                predictions.append((keyword, start_time, end_time, confidence))
        
        # Aggregate predictions
        return self._aggregate_predictions(predictions, min_detections)

    def _process_audio_chunks(self, file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        """
        Process audio file in chunks of SAMPLES_TO_CONSIDER length
        
        Returns:
            list: List of MFCC features for each chunk
        """
        # Load audio file
        signal, sample_rate = librosa.load(file_path, sr=22050)
        
        # Split signal into chunks
        chunks = []
        for i in range(0, len(signal), SAMPLES_TO_CONSIDER):
            chunk = signal[i:i + SAMPLES_TO_CONSIDER]
            
            # Pad last chunk if necessary
            if len(chunk) < SAMPLES_TO_CONSIDER:
                chunk = np.pad(chunk, (0, SAMPLES_TO_CONSIDER - len(chunk)))
                
            # Extract MFCCs
            mfccs = librosa.feature.mfcc(
                y=chunk,
                sr=sample_rate,
                n_mfcc=num_mfcc,
                n_fft=n_fft,
                hop_length=hop_length
            )
            chunks.append(mfccs.T)
            
        return chunks

    def _aggregate_predictions(self, predictions, min_detections):
        """
        Aggregate predictions to remove duplicates and combine nearby detections.
        
        Args:
            predictions (list): List of (keyword, start_time, end_time, confidence) tuples
            min_detections (int): Minimum number of detections needed to report a keyword
        
        Returns:
            list: Filtered and combined predictions
        """
        if not predictions:
            return []
            
        # Group predictions by keyword
        keyword_groups = {}
        for keyword, start, end, conf in predictions:
            if keyword not in keyword_groups:
                keyword_groups[keyword] = []
            keyword_groups[keyword].append((start, end, conf))
            
        # Filter and combine predictions
        final_predictions = []
        for keyword, detections in keyword_groups.items():
            if len(detections) >= min_detections:
                # Combine nearby detections
                detections.sort(key=lambda x: x[0])  # Sort by start time
                current_group = [detections[0]]
                
                for detection in detections[1:]:
                    if detection[0] - current_group[-1][1] <= 0.5:  # If less than 0.5s gap
                        current_group.append(detection)
                    else:
                        # Process current group
                        if len(current_group) >= min_detections:
                            avg_conf = np.mean([d[2] for d in current_group])
                            final_predictions.append({
                                'keyword': keyword,
                                'start_time': current_group[0][0],
                                'end_time': current_group[-1][1],
                                'confidence': avg_conf,
                                'num_detections': len(current_group)
                            })
                        current_group = [detection]
                
                # Process last group
                if len(current_group) >= min_detections:
                    avg_conf = np.mean([d[2] for d in current_group])
                    final_predictions.append({
                        'keyword': keyword,
                        'start_time': current_group[0][0],
                        'end_time': current_group[-1][1],
                        'confidence': avg_conf,
                        'num_detections': len(current_group)
                    })
                    
        return final_predictions

def Keyword_Spotting_Service():
    """Factory function for KeywordSpottingService class."""
    if KeywordSpottingService._instance is None:
        KeywordSpottingService._instance = KeywordSpottingService()
        KeywordSpottingService.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    return KeywordSpottingService._instance

if __name__ == "__main__":
    # Create keyword spotting service
    kss = Keyword_Spotting_Service()
    
    # Make a prediction
    predictions = kss.predict(
        "test/test2.wav",
        confidence_threshold=0.9,
        min_detections=1
    )
    
    # Print results
    for pred in predictions:
        print(f"Detected '{pred['keyword']}' from {pred['start_time']:.2f}s to "
              f"{pred['end_time']:.2f}s (confidence: {pred['confidence']:.2f})")
