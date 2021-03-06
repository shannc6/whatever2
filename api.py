from io import BytesIO

from PIL import Image

import cv2
from flask import Flask, abort, jsonify, request
from image_comparison import compare_images
from auth import AuthError, requires_auth
import config
import datetime
import jwt
from jwt import PyJWKClient

class Image:
    def create_app(self, test_config=None):
        app = Flask(__name__)

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
    image = Image()
    app = image.create_app()
    app.run(debug=True)
