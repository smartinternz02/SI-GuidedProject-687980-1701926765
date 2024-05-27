import os
import base64
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from generate_caption import generate_caption
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Concatenate  # Add this line to import Concatenate

app = Flask(__name__)
GC = generate_caption()

# Loading the model
model = load_model("best_model.h5", compile=False) 

# default home page or route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Prediction')
def Prediction():
    return render_template('Prediction.html')

@app.route('/PredictCaption', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['image']
        # Getting the current path i.e where app.py is present
        basepath = os.path.dirname(__file__)
        print("Current path:", basepath)
        # Saving the uploaded file to the uploads folder
        filepath = os.path.join(basepath, 'uploads', file.filename)
        print("Upload folder is:", filepath)
        file.save(filepath)

        captions = GC.generate_captions(filepath)

        with open(filepath, 'rb') as uploadedfile:
            img_base64 = base64.b64encode(uploadedfile.read()).decode()

        return render_template('Prediction.html', prediction=str(captions), image=img_base64)

""" Running our application """
if __name__ == '__main__':
    app.run(debug=True, port=1100)
