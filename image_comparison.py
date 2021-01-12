# import the necessary packages
#from skimage.measure import structural_similarity as ssim
from skimage import measure

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import requests
import urllib
import cv2 
from PIL import Image
from io import BytesIO
import urllib.request
import validators
import matplotlib.pyplot as plt

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

def isUrl(path):
    valid = validators.url(path)
    return valid

def processUrl(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.save('local.jpg')
    imgRead = cv2.imread('local.jpg')
    return imgRead

def compare_images(imageAPath, imageBPath):
    # compute the mean squared error and structural similarity
    imageA = processUrl(imageAPath) if isUrl(imageAPath) else cv2.imread(imageAPath)
    imageB = processUrl(imageBPath) if isUrl(imageBPath) else cv2.imread(imageBPath)
    s = measure.compare_ssim(imageA, imageB, multichannel=True)
    return s

def compare_images2(imageAPath, imageBPath):
    # compute the mean squared error and structural similarity
    
    response = requests.get('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7', stream=True)
    img = Image.open(response.raw)

    plt.imshow(img)
    plt.show()

def test(a):
    if a == 1:
        t = 0
    print(t)

if __name__ == "__main__":
    a = 0
    #test()
    # imageA = cv2.imread("IMG_7162.JPG")
    # imageB = cv2.imread("black.jpg")
    # imageC = cv2.imread("white.jpg")
    #imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)  
    #imageB = imageA
    # compare_images2('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7','https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7')
    # compare_images('black.jpg', 'https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80')
    # s1 = compare_images('black.jpg', 'white.jpg')
    s2 = compare_images('https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80', 'https://consequenceofsound.net/wp-content/uploads/2019/05/pikachu-e1557247424342.jpg?quality=80')
    # print(s1)
    print(s2)
    # test(1)
