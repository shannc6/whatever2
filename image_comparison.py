import urllib
import urllib.request
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image
from skimage import io, measure

import cv2
import validators


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

def isUrl(path):
    # TODO: Not sure why you need the wrapper 
    """Checks if the given path is a valid url.
    
    Args:
    """
    valid = validators.url(path)
    return valid

def processUrl(url):
    """Gets the image from the given url.

    Retrieves the image from the given url and save it as a image.  

    Args:
      url:
        The url to retrieve the image from.
      
    Returns:
      An image that is loaded from the url.

    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.save('local.jpg')
    imgRead = cv2.imread('local.jpg')
    return imgRead

def compare_images(imageAPath, imageBPath):
    """ Compares the structural similarity of the two given images.

    Args:
        imageAPath:
        imageBPath:

    Returns:
        # TODO: Return percentage, or what unit?
        The percentage of the similarity of two given images.
        (0 completely different, 1 the same)  
    
    """
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


if __name__ == "__main__":
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
