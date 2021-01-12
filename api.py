from flask import Flask, request, jsonify, abort
from image_comparison import compare_images
import cv2
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('url')
    img = Image.open(BytesIO(response.content))
    return img

@app.route('/image-comparison', methods=['GET'])
def get_percent():
    try:
        imageA = request.args.get('imageA')
        imageB = request.args.get('imageB')
        ssim = compare_images(imageA, imageB)
        return jsonify({
            'success': True,
            'percentage': ssim
        })
    except:
       abort(401)

if __name__ == "__main__":
    app.run(debug=True)