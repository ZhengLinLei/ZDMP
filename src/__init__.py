"""
    Apache License 2.0
    Repository: https://github.com/ZhengLinLei/ZDMP


    Here is the code for the server API in Flask




    Repository: https://github.com/ZhengLinLei/ZDMP-Client
    This repository is part of our main project system ZDMP, which is a system for the prediction of the reliability of a product.
    

    Steps of using:
       1. Python server API
       2. Node server
       3. Every client will use their browser to connect to the Node server and return the website to the client
       4. The website will create a script to receive the input prediction data from the Message Bus and then will send the data to the Python server API
       5. The Python server API will return the prediction to the website and then the website will send the prediction output to the Message Bus and at the same time will send the prediction to the client to visualizate it
       6. The website also can receive the output history from the Message Bus and then to visualizate it

"""


# Create a local server that will receive the data and return the prediction
# The data will be sent to the server in JSON format
# The server will return the prediction in JSON format
# The server will be created using Flask

# Import libraries
import os, json
from flask import Flask, request, jsonify

# Import the model
from .predict import predict

# Load training configuration ./config.ini
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)) # ./src
CONFIG = json.load(open(os.path.join(CURRENT_PATH, 'config.ini'))) # ./config.ini

# Create the app
app = Flask(__name__)

# Create the route
@app.route('/predict', methods=['POST'])
def predict_api():
    # Get the data
    data = request.get_json(force=True)

    # Make prediction
    prediction = predict(data, os.path.join(CURRENT_PATH, CONFIG['model']['path']))

    # Return the prediction
    return jsonify(prediction)

# Train the model
@app.route('/train', methods=['GET'])
def train_api():
    # Train the model
    # --> Run the train.py script

    # import subprocess
    # subprocess.call(['python', os.path.join(CURRENT_PATH, 'train.py')])

    TRAIN_PATH = os.path.join(CURRENT_PATH, 'train.py')
    with open(TRAIN_PATH) as f:
        code = compile(f.read(), TRAIN_PATH, 'exec')
        exec(code)

    # Return the result
    return jsonify({'status': 'ok'})

# Run the app
if __name__ == '__main__':
    app.run(port=CONFIG['server']['port'], debug=True)