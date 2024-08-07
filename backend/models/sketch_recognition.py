import tensorflow as tf
import numpy as np
import base64
from io import BytesIO
from PIL import Image
import json

def load_model():
    model = tf.keras.models.load_model('path/to/your/sketch_recognition_model.h5')
    return model

model = load_model()

def recognize_sketch(sketch):
    processed_sketch = preprocess_sketch(sketch)
    predictions = model.predict(processed_sketch)
    return decode_predictions(predictions)

def preprocess_sketch(sketch):
    # Convert base64 string back to image
    img = Image.open(BytesIO(base64.b64decode(sketch.split(',')[1])))
    img = img.resize((28, 28)).convert('L')  # Resize and convert to grayscale
    img = np.array(img) / 255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def decode_predictions(predictions):
    # Assuming your model outputs class probabilities, decode them to class names
    class_names = ['class1', 'class2', 'class3']  # Replace with your actual class names
    top_predictions = np.argsort(predictions[0])[::-1][:3]
    return [class_names[i] for i in top_predictions]