from flask import jsonify
from app import app
from flask import request
import os


def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404
    return resp


UPLOAD_FOLDER = os.path.abspath('controller/detector/input')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files.to_dict()['image']
        print(file)
        # # if user does not select file, browser also
        # # submit a empty part without filename

        if file:
            filename = 'input.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('Input image saved')

        else:
            print('file not found')





#
