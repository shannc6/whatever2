import urllib
import urllib.request
import numpy as np
import requests
from PIL import Image
from skimage import io, measure
import cv2
import validators
import os
from io import BytesIO
from PIL import Image
import cv2
from flask import Flask, abort, jsonify, request
from image_comparison import compare_images
from auth import AuthError, requires_auth

class ImageComparison:
    def isSameImg(self, imageA, imageB):
        if imageA.shape == imageB.shape:
            diff = cv2.subtract(imageA, imageB)
            b, g, r = cv2.split(diff)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                return True
        return False

    def compare_images(self, imageAPath, imageBPath):
        """ Compares the structural similarity of the two given images.

        Args:
            imageAPath:
            imageBPath:

        Returns:
            Return string: percentage
            The percentage of the similarity of two given images.
            (0 completely different, 1 the same)  
        
        """
        # read the image from local files or url
        imageA = io.imread(imageAPath) if validators.url(imageAPath) else cv2.imread(imageAPath)
        imageB = io.imread(imageBPath) if validators.url(imageBPath) else cv2.imread(imageBPath)
        # check the same image. If image the same, no need to compute the rest
        if self.isSameImg(imageA, imageB):
            return "100%"
        
        # Check for similarities between the 2 images
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(imageA, None)
        kp_2, desc_2 = sift.detectAndCompute(imageB, None)
        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.6*n.distance:
                good_points.append(m)

        number_keypoints = len(kp_1) if len(kp_1) <= len(kp_2) else len(kp_2)
        percentage = '{0:.2f}'.format(len(good_points) / number_keypoints * 100) + "%"
        return percentage

class Image:
    def create_app(self, test_config=None):
        app = Flask(__name__)
        @app.route('/image-comparison', methods=['GET'])
        @requires_auth('get:image-comparison')
        def get_percent(jwt):
            try:
                imageA = request.args.get('imageA')
                imageB = request.args.get('imageB')
                image_comparison = ImageComparison()
                percentage = image_comparison.compare_images(imageA, imageB)
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