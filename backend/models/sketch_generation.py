import tensorflow as tf
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def load_gan_model():
    gan_model = tf.keras.models.load_model('path/to/your/sketch_generation_model.h5')
    return gan_model

gan_model = load_gan_model()

def generate_sketch(sketch):
    processed_sketch = preprocess_sketch(sketch)
    generated_image = gan_model.predict(processed_sketch)
    return postprocess_generated_image(generated_image)

def preprocess_sketch(sketch):
    # Convert base64 string back to image
    img = Image.open(BytesIO(base64.b64decode(sketch.split(',')[1])))
    img = img.resize((28, 28)).convert('L')  # Resize and convert to grayscale
    img = np.array(img) / 255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def postprocess_generated_image(image):
    # Assuming image is [1, 28, 28, 1] shape, convert back to base64 string
    image = np.squeeze(image)  # Remove batch and channel dimensions
    image = (image * 255).astype(np.uint8)  # De-normalize to [0, 255]
    img = Image.fromarray(image, 'L')  # Convert to PIL image
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")