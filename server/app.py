import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from PIL import Image
from werkzeug.utils import secure_filename
from CustomPredictionCustomModel import prediction_custom

UPLOAD_FOLDER = "C:\\Users\makis\Documents"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
class1 = ""
pred = ""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def manipulate_image(stream, saved_location, filename):

    image_obj = Image.open(stream)
    image_obj.save(saved_location)
    global class1, pred

    pat = UPLOAD_FOLDER + "\\" + str(filename)

    class1, pred = prediction_custom(pat)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            saved_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            manipulate_image(file, saved_location, filename)

            return jsonify({
                "class": class1,
                "prediction": pred
            })

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
