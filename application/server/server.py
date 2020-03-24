# import pymysql
from app import app
from flask import jsonify
from flask import request
from flask_cors import CORS
from controller.accept import file_detect


CORS(app)


###############################################################################
##                                ROUTES
###############################################################################


# file accept route
@app.route("/detect", methods=["POST"])
# @cross_origin()
def accept_file():
    return file_detect()


# 404 handler
@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(port=4000) # Change port as required. Also don't forget to change the port in home.js file in client
