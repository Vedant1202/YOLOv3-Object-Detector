# import pymysql
from flask import jsonify
from flask import request
from utils.utils import not_found, upload_file
from werkzeug.utils import secure_filename
from controller.detector.image import main
import os

def file_detect():
    try:
        file = request.files.to_dict()['image']
        filename = secure_filename(file.filename)

        # validate the received values
        if file and request.method == "POST":
            upload_file()
            result = main(os.path.join(os.getcwd(), 'controller/detector/input/input.jpg'))

            resp = jsonify(results=result)
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print('====================== EXCEPTION ========================')
        print(e)
    finally:
        print('Done')
