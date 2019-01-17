import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.insert(0, './tensorflow/')
import nn

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# don't worry, I know this is a terrible idea
network = None

# mildly flawed, you have to make a request to configure the server
@app.route('/startnn', methods=['GET'])
def configure_and_test_nn():
    global network
    network = nn.configure_nn()

    # TODO make this asynchronous
    return 'Done!'

@app.route('/', methods=['GET'])
def hello():
    global network
    if network is None:
        return 'NN Still Configuring'
        
    return "Welcome to our flask api!"

@app.route('/predict', methods=['POST'])
def upload_file():
    global network
    if network is None:
        return 'NN Still Configuring'
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'Fam you didn\'t send a file header'
    file = request.files['file']
    # check if the file is in the request
    if file.filename == '':
        return 'Fam you didn\'t send a file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        prediction = network.get_prediction(file)
        return str(int(prediction))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS