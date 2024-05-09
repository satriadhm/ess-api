import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def predict_image_class(model, img_path):
    # Load the image to be predicted
    img = image.load_img(img_path, target_size=(150, 150))

    # Convert the image to an array
    img_array = image.img_to_array(img)

    # Expand the dimensions to match the input shape expected by the model
    img_array = np.expand_dims(img_array, axis=0)

    # Normalize the pixel values
    img_array /= 255.

    # Make prediction
    predictions = model.predict(img_array)

    # Get the predicted class label
    predicted_class = np.argmax(predictions)

    # Map predicted class to production class label
    if predicted_class == 0:
        return "0-25 ton/ha"
    elif predicted_class == 1:
        return "25-50 ton/ha"
    else:
        return "50 ton++"