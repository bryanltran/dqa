# CS-4273-Capstone-Group-B
Repository for Fall 2024 CS 4273 Capstone Project

## NOTE 

This README is subject to many changes. The current instructions are crude and are the bare minimum to get the code working, there will be a more streamlined process in the future.

## Overview (TODO)

This project pre-processes a voice dataset by extracting Mel-Frequency Cepstral Coefficients (MFCCs), which represent the essential features of audio signals. These MFCCs are then saved in a JSON file, providing a structured way to store important acoustic features for machine learning models. 

### Prerequisites

Must have Python installed

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Install the required library (`librosa`):**

   ```bash
   pip install librosa
   ```

3. **Download the dataset:**

   [Download speech_commands_v0.01.tar.gz](http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz)


### Processing Data

1. **Create a `data/` folder**:
   In the root of your project, create a directory called `data/` to store your dataset files.
   ```bash
   mkdir data
   ```

2. **Extract the dataset**:
   If you have a dataset file in `tar.gz` format, extract it into the `data/` folder. Replace `your_dataset.tar.gz` with the name of your dataset file:
   ```bash
   tar -xzvf your_dataset.tar.gz -C data/
   ```

3. **Run the dataset preparation script**:
   After extracting the dataset, you can run the dataset preparation script located in the `scripts/` directory. Use the following command:
   ```bash
   python scripts/prepare_dataset.py
   ```

