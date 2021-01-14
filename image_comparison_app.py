import requests
from PIL import Image
from skimage import io
import cv2
import validators
from auth import AuthError, requires_auth
from flask import Flask, abort, jsonify, request

class ImageComparison:
    """ Class for image comparison.

    ImageComparison compares the similarity of two images.

    """
    def is_same_img(self, image_a, image_b):
        """ Checks if the given two images are the same.

        Args:
            image_a: The first image for image comparison
            image_b: The second image for image comparison 

        Returns:
            Boolean. True if the two given images are the same; False,
            otherwise. 
        """
        if image_a.shape == image_b.shape:
            diff = cv2.subtract(image_a, image_b)
            b, g, r = cv2.split(diff)
            return (cv2.countNonZero(b) == 0 and
                    cv2.countNonZero(g) == 0 and
                    cv2.countNonZero(r) == 0)
        return False

    def compare_images(self, image_a_path, image_b_path):
        """ Compares the similarity of the two given images.

        The image comparison is caculated using fast library for approximate
        nearest neighbors and scale-invariant feature transform

        Args:
            image_a_path: First image path for comparison.
            image_b_path: Second image path for comparison.

        Returns:
            Float. The percentage of the similarity of two given images.
            (0 completely different, 100 the same)

        """
        # Read the image from local files or url
        image_a = io.imread(image_a_path) if validators.url(
            image_a_path) else cv2.imread(image_a_path)
        image_b = io.imread(image_b_path) if validators.url(
            image_b_path) else cv2.imread(image_b_path)

        # check the same image. If image the same, no need to compute the rest
        if self.is_same_img(image_a, image_b):
            return 100

        # Check for similarities between the 2 images
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(image_a, None)
        kp_2, desc_2 = sift.detectAndCompute(image_b, None)
        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.6*n.distance:
                good_points.append(m)

        number_keypoints = len(kp_1) if len(kp_1) <= len(kp_2) else len(kp_2)
        percentage = len(good_points) / number_keypoints * 100
        return percentage


class ImageAPI:
    """API for image comparison.
    
    GET method and need authentication key.
    """

    def create_app(self, test_config=None):
        app = Flask(__name__)

        @app.route('/image-comparison', methods=['GET'])
        @requires_auth('get:image-comparison')
        def get_percent(jwt):
            try:
                imageA = request.args.get('imageA')
                imageB = request.args.get('imageB')
                image_comparison = ImageComparison()
                percentage = '{0:.2f}'.format(
                    image_comparison.compare_images(imageA, imageB)) + "%"
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
