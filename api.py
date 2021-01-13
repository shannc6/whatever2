from io import BytesIO

import requests
from PIL import Image

import cv2
from flask import Flask, abort, jsonify, request
from image_comparison import compare_images
from auth import AuthError, requires_auth

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('url')
    img = Image.open(BytesIO(response.content))
    return img

@app.route('/image-comparison', methods=['GET'])
@requires_auth('get:image-comparison')
def get_percent(jwt):
    try:
        imageA = request.args.get('imageA')
        imageB = request.args.get('imageB')
        ssim = compare_images(imageA, imageB)
        return jsonify({
            'success': True,
            'percentage': ssim
        })
    except:
       abort(404)

if __name__ == "__main__":
    app.run(debug=True)
