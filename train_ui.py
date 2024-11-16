import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

def browse_dataset():
    print("browse")
    
def train_model():
    print("train")
    
# Create the main application window
train_ui = tk.Tk()
train_ui.title("Speech Command Trainer")
train_ui.geometry("400x200")

# Dataset path variable
dataset_path = tk.StringVar()

# Create and place UI elements
frame = tk.Frame(train_ui, padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

label = tk.Label(frame, text="Select Speech Command Dataset:")
label.pack(pady=5)

entry = tk.Entry(frame, textvariable=dataset_path, width=40)
entry.pack(pady=5, padx=5, fill=tk.X)

browse_button = tk.Button(frame, text="Browse", command=browse_dataset)
browse_button.pack(pady=5)

train_button = tk.Button(frame, text="Train Model", command=train_model, bg="green", fg="white")
train_button.pack(pady=20)

# Run the application
train_ui.mainloop()   