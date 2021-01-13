from io import BytesIO

from PIL import Image

import cv2
from flask import Flask, abort, jsonify, request
from image_comparison import compare_images
from auth import AuthError, requires_auth
from config import *
import datetime

class Image:
    def __init__(self):
        self.blank = 0

    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        print("yo")
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow()
            }
            return jwt.encode(
                payload,
                config.Bearer,
                algorithm='RS256'
            )
        except Exception as e:
            return e

    def create_app(test_config=None):
        app = Flask(__name__)
        self.encode_auth_token()

        @app.route('/image-comparison', methods=['GET'])
        @requires_auth('get:image-comparison')
        def get_percent(jwt):
            try:
                imageA = request.args.get('imageA')
                imageB = request.args.get('imageB')
                percentage = compare_images(imageA, imageB)
                return jsonify({
                    'success': True,
                    'percentage': percentage
                })
            except:
                abort(404)

        # Error Handling
        @app.errorhandler(422)
        def unprocessable(error):
            return jsonify({
                "success": False,
                "error": 422,
                "message": "unprocessable"
            }), 422

        @app.errorhandler(404)
        def not_found(error):
            return jsonify({
                "success": False,
                "error": 404,
                "message": "resource not found"
            }), 404

        @app.errorhandler(AuthError)
        def handle_auth_error(e):
            return jsonify({
                "success": False,
                "error": e.status_code,
                'message': e.error
            }), 401
        return app

if __name__ == "__main__":
    app = Image.create_app()
    app.run(debug=True)
