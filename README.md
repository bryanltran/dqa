# Dispatch Quality Analysis
Repository for Fall 2024 CS 4273 Capstone Project

## NOTE

This README is subject to many changes. The current instructions are crude and are the bare minimum to get the code working. There will be a more streamlined process in the future.

## Overview

This project pre-processes a voice dataset by extracting Mel-Frequency Cepstral Coefficients (MFCCs), which represent the essential features of audio signals. These MFCCs are then saved in a JSON file, providing a structured way to store important acoustic features for machine learning models. The extracted features are then used to train a model for recognizing speech commands.

### Prerequisites

Must have Python installed.

1. **Create a virtual environment:**
* Windows:
   ```bash
   .\venv\Scripts\activate
   ```
* Linux/MacOS:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies from requirement.txt document (open the txt file first to confirm):**

   ```bash
   pip install -r requirements.txt
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

### Training the Model

After preparing the dataset, you can train the model using the following command:

   ```bash
   python scripts/train.py
   ```

This will train the model on the pre-processed dataset and save the trained model for future use.

### Predicting with the Model

1. **Create a `tests/` folder**:
   In the root directory of your project, create a `tests/` folder to store the test audio files.

   ```bash
   mkdir tests
   ```

2. **Run the prediction script**:
   After adding test files to the `tests/` folder, you can run the prediction script. Make sure to adjust the file path in the script if necessary:

   ```bash
   python scripts/detect.py
   ```

This will use the trained model to predict the speech command from the audio file in the `tests/` folder.

UI Design prototype from Figma:
* Home Menu:
![Screenshot 2024-10-07 183816](https://github.com/user-attachments/assets/9dbfec89-5db8-4872-930e-c56d452d2cea)

* Transcribe:
![Screenshot 2024-10-07 183824](https://github.com/user-attachments/assets/e5919bc1-5c64-43d8-94f7-e9ee36e89d84)

