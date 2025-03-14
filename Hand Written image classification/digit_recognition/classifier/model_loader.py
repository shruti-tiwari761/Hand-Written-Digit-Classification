import tensorflow as tf
import numpy as np

# Load the pre-trained model
model = tf.keras.models.load_model("classifier/digit_classifier.h5")

def predict_digit(image):
    image = image.reshape(1, 28, 28, 1)  # Reshape for model input
    prediction = model.predict(image)
    return prediction.argmax()  # Return the predicted digit
