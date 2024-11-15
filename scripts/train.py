import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Configuration parameters
DATA_PATH = "data.json"
SAVED_MODEL_PATH = "models/model.keras"
EPOCHS = 40
BATCH_SIZE = 32
PATIENCE = 5
LEARNING_RATE = 0.0001

def load_data(data_path):
    """
    Loads data from a JSON file, extracting features and labels.

    Args:
        data_path (str): Path to JSON file containing data.

    Returns:
        tuple: Features (X) and labels (y) as numpy arrays.
    """
    with open(data_path, "r") as fp:
        data = json.load(fp)
    X = np.array(data["MFCCs"])
    y = np.array(data["labels"])
    print("Data loaded successfully!")
    return X, y

def prepare_dataset(data_path, test_size=0.2, validation_size=0.2):
    """
    Splits data into training, validation, and test sets.

    Args:
        data_path (str): Path to JSON file.
        test_size (float): Fraction of data to use for testing.
        validation_size (float): Fraction of training data to use for validation.

    Returns:
        tuple: Training, validation, and test sets.
    """
    X, y = load_data(data_path)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # Split training data into train and validation sets
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)
    
    # Reshape data to add a channel dimension for CNN compatibility
    X_train = X_train[..., np.newaxis]
    X_validation = X_validation[..., np.newaxis]
    X_test = X_test[..., np.newaxis]
    
    return X_train, y_train, X_validation, y_validation, X_test, y_test

def build_model(input_shape, loss="sparse_categorical_crossentropy", learning_rate=LEARNING_RATE):
    """
    Builds and compiles a convolutional neural network model.

    Args:
        input_shape (tuple): Shape of the input data.
        loss (str): Loss function.
        learning_rate (float): Learning rate for optimizer.

    Returns:
        model: Compiled CNN model.
    """
    model = tf.keras.models.Sequential([
        # First convolutional block
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=input_shape,
                               kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'),
        
        # Second convolutional block
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'),
        
        # Third convolutional block
        tf.keras.layers.Conv2D(32, (2, 2), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2), strides=(2, 2), padding='same'),
        
        # Flatten and dense layers
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        
        # Output layer
        tf.keras.layers.Dense(2, activation='softmax')
    ])

    # Compile model with Adam optimizer
    optimizer = tf.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])
    model.summary()
    
    return model

def train(model, epochs, batch_size, patience, X_train, y_train, X_validation, y_validation):
    """
    Trains the model and applies early stopping based on validation accuracy.

    Args:
        model: Compiled model.
        epochs (int): Number of epochs.
        batch_size (int): Batch size.
        patience (int): Early stopping patience.

    Returns:
        history: Training history.
    """
    # Early stopping to prevent overfitting
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", min_delta=0.001, patience=patience)
    
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_validation, y_validation),
        callbacks=[early_stopping]
    )
    return history

def main():
    # Prepare dataset splits
    X_train, y_train, X_validation, y_validation, X_test, y_test = prepare_dataset(DATA_PATH)
    
    # Initialize model
    input_shape = (X_train.shape[1], X_train.shape[2], 1)
    model = build_model(input_shape, learning_rate=LEARNING_RATE)
    
    # Train model
    history = train(model, EPOCHS, BATCH_SIZE, PATIENCE, X_train, y_train, X_validation, y_validation)
    
    # Evaluate performance on test set
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"\nTest Loss: {test_loss}, Test Accuracy: {test_acc * 100:.2f}%")
    
    # Save trained model in the Keras format
    model.save(SAVED_MODEL_PATH)


if __name__ == "__main__":
    main()
