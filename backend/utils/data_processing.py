import numpy as np
import base64
from io import BytesIO
from PIL import Image

def preprocess_sketch(sketch):
    """
    Convert a base64-encoded sketch image to a normalized numpy array suitable for model input.
    """
    # Decode the base64 string to get the image data
    img_data = base64.b64decode(sketch.split(',')[1])
    
    # Open the image using PIL
    img = Image.open(BytesIO(img_data))
    
    # Resize the image to the required input size of the model (e.g., 28x28)
    img = img.resize((28, 28)).convert('L')  # Convert to grayscale
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Normalize the image data to the range [0, 1]
    img_array = img_array / 255.0
    
    # Add the required dimensions for model input (batch size and channel)
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
    img_array = np.expand_dims(img_array, axis=0)   # Add batch dimension
    
    return img_array

def postprocess_generated_image(image):
    """
    Convert a numpy array representing an image back to a base64-encoded string.
    """
    # Remove the batch dimension and the channel dimension if they exist
    if len(image.shape) == 4:
        image = np.squeeze(image, axis=0)  # Remove batch dimension
        image = np.squeeze(image, axis=-1)  # Remove channel dimension
    
    # De-normalize the image data from the range [0, 1] to [0, 255]
    image = (image * 255).astype(np.uint8)
    
    # Convert the numpy array back to a PIL image
    img = Image.fromarray(image, 'L')  # 'L' mode for grayscale images
    
    # Save the PIL image to a BytesIO buffer
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    
    # Encode the image data as a base64 string
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    # Return the base64-encoded string
    return img_base64