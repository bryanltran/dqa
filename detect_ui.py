import tkinter as tk
from tkinter import filedialog, messagebox
import os
from scripts.detect import Keyword_Spotting_Service

def browse_wav_file():
    """Allow the user to select a WAV file."""
    file_path = filedialog.askopenfilename(
        title="Select a WAV File",
        filetypes=[("WAV Files", "*.wav")]
    )
    if file_path:
        wav_file_path.set(file_path)

def detect_keywords():
    """Use KeywordSpottingService to detect keywords in the selected WAV file."""
    file_path = wav_file_path.get()
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "Please select a valid WAV file.")
        return
    
    try:
        # Perform keyword spotting
        kss = Keyword_Spotting_Service()
        predictions = kss.predict(file_path, confidence_threshold=0.5, min_detections=1)
        
        # Display predictions in the result box
        result_box.delete(1.0, tk.END)
        if predictions:
            for pred in predictions:
                result_box.insert(
                    tk.END,
                    f"Detected '{pred['keyword']}' from {pred['start_time']:.2f}s to "
                    f"{pred['end_time']:.2f}s (confidence: {pred['confidence']:.2f})\n"
                )
        else:
            result_box.insert(tk.END, "No keywords detected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# Create the main application window
detect_ui = tk.Tk()
detect_ui.title("Keyword Spotting")
detect_ui.geometry("500x400")

# WAV file path variable
wav_file_path = tk.StringVar()

# Create and place UI elements
frame = tk.Frame(detect_ui, padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

label = tk.Label(frame, text="Select a WAV File:")
label.pack(pady=5)

entry = tk.Entry(frame, textvariable=wav_file_path, width=40)
entry.pack(pady=5, padx=5, fill=tk.X)

browse_button = tk.Button(frame, text="Browse", command=browse_wav_file)
browse_button.pack(pady=5)

detect_button = tk.Button(frame, text="Detect Keywords", command=detect_keywords, bg="green", fg="white")
detect_button.pack(pady=20)

result_label = tk.Label(frame, text="Detection Results:")
result_label.pack(pady=5)

result_box = tk.Text(frame, height=10, width=50)
result_box.pack(pady=5, padx=5, fill=tk.BOTH)

# Run the application
detect_ui.mainloop()