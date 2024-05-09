import src.capture as capture
from flask import Flask, request, jsonify
import ee
import joblib 

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    ee.Initialize(project = "ee-glorioussatria")
    return jsonify({'message': 'Welcome to the Earth Engine API!'})

@app.route('/capture', methods=['POST'])
def capture_image():

    # Get the request data
    data = request.get_json()
    firstCoordinate = data['firstCoordinate']
    print(firstCoordinate)
    secondCoordinate = data['secondCoordinate']
    print(secondCoordinate)
    thirdCoordinate = data['thirdCoordinate']
    print(thirdCoordinate)
    fourthCoordinate = data['fourthCoordinate']
    
    # Capture the image
    url = capture.capture_image(firstCoordinate, secondCoordinate, thirdCoordinate, fourthCoordinate)
    
    # Return a response
    return jsonify({'message': 'Image captured', 'url': url})

@app.route('/predict-mobile', methods=['POST'])

def predict_image_mobile():
    model = joblib.load('model/modelVGG.tflite', 'rb')
    response = model.predict_image_class(model, 'data1.jpg')
    return jsonify({'message': 'Image predicted', 'class': response})
    
    
@app.route('/predict-web', methods=['POST'])

def predict_image_web():
    model = joblib.load('model/modelVGG.pkl', 'rb')
    response = model.predict_image_class(model, 'data1.jpg')
    return jsonify({'message': 'Image predicted', 'class': response})


