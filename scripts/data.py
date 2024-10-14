import librosa
import os
import json

DATASET_PATH = "data"
JSON_PATH = "data.json"
SAMPLES_TO_CONSIDER = 22050  # 1 second of audio


def preprocess_dataset(dataset_path, json_path, num_mfcc=13, n_fft=2048, hop_length=512):
    """
    Extract MFCCs from the dataset and save to a JSON file.
    
    :param dataset_path (str): Path to the dataset folder.
    :param json_path (str): Path to save the JSON file.
    :param num_mfcc (int): Number of MFCC features to extract.
    :param n_fft (int): Number of samples per FFT window.
    :param hop_length (int): Step size between FFT windows.
    """
    
    # Create a dictionary to store labels, MFCCs, and file paths
    data = {
        "mapping": [],
        "labels": [],
        "MFCCs": [],
        "files": []
    }

    # Traverse the dataset directory
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # Skip the root directory
        if dirpath != dataset_path:

            # Extract the folder name to use as a label
            label = os.path.basename(dirpath)
            data["mapping"].append(label)
            print(f"\nProcessing: '{label}'")

            # Process each audio file in the folder
            for f in filenames:
                file_path = os.path.join(dirpath, f)

                # Load the audio file
                signal, sample_rate = librosa.load(file_path)

                # Only process files with enough samples
                if len(signal) >= SAMPLES_TO_CONSIDER:
                    # Trim or pad the audio to a fixed length
                    signal = signal[:SAMPLES_TO_CONSIDER]

                    # Extract MFCC features
                    MFCCs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)

                    # Save MFCCs, label, and file path
                    data["MFCCs"].append(MFCCs.T.tolist())
                    data["labels"].append(i-1)  # Use folder index as label
                    data["files"].append(file_path)
                    print(f"{file_path}: {i-1}")

    # Write the results to a JSON file
    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


if __name__ == "__main__":
    preprocess_dataset(DATASET_PATH, JSON_PATH)
