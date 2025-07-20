import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import urllib.request

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# DNN model files
MODEL_DIR = 'models'
PROTOTXT = os.path.join(MODEL_DIR, 'deploy.prototxt')
CAFFEMODEL = os.path.join(MODEL_DIR, 'res10_300x300_ssd_iter_140000.caffemodel')
PROTOTXT_URL = 'https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt'
CAFFEMODEL_URL = 'https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel'

app = Flask(__name__, template_folder='templates', static_folder=RESULT_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def download_model_files():
    if not os.path.exists(PROTOTXT):
        print('Downloading prototxt...')
        urllib.request.urlretrieve(PROTOTXT_URL, PROTOTXT)
    if not os.path.exists(CAFFEMODEL):
        print('Downloading caffemodel...')
        urllib.request.urlretrieve(CAFFEMODEL_URL, CAFFEMODEL)

def detect_faces_dnn(image, conf_threshold=0.3, upscale_factor=1.5):
    download_model_files()
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, CAFFEMODEL)
    (h, w) = image.shape[:2]
    # Upscale if not already huge
    if max(h, w) < 1200:
        image = cv2.resize(image, (int(w*upscale_factor), int(h*upscale_factor)))
        h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    faces = []
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')
            faces.append((startX, startY, endX - startX, endY - startY))
    return faces, image

@app.route('/', methods=['GET', 'POST'])
def index():
    result_url = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Face detection using DNN (improved for small faces)
            img = cv2.imread(filepath)
            faces, img_up = detect_faces_dnn(img)
            for (x, y, w, h) in faces:
                cv2.rectangle(img_up, (x, y), (x+w, y+h), (0, 255, 0), 2)
            result_filename = 'result_' + filename
            result_path = os.path.join(RESULT_FOLDER, result_filename)
            cv2.imwrite(result_path, img_up)
            result_url = url_for('static', filename=result_filename)
            return render_template('index.html', result_url=result_url, faces=len(faces))
        else:
            return render_template('index.html', error='Invalid file type')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 