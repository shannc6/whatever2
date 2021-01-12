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

import matplotlib.pyplot as plt


# def mse(imageA, imageB):
# 	# the 'Mean Squared Error' between the two images is the
# 	# sum of the squared difference between the two images;
# 	# NOTE: the two images must have the same dimension
# 	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
# 	err /= float(imageA.shape[0] * imageA.shape[1])
	
# 	# return the MSE, the lower the error, the more "similar"
# 	# the two images are
# 	return err

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

def compare_images(imageAPath, imageBPath):
    # compute the mean squared error and structural similarity
    imageA = cv2.imread(imageAPath)
    imageB = cv2.imread(imageBPath)
    s = measure.compare_ssim(imageA, imageB, multichannel=True)
    # setup the figure
    #fig = plt.figure(title)
    #plt.suptitle("SSIM: %.2f" % (s))
    # show first image
    #ax = fig.add_subplot(1, 2, 1)
    #plt.imshow(imageA, cmap = plt.cm.gray)
    #plt.axis("off")
    # show the second image
    #ax = fig.add_subplot(1, 2, 2)
    #plt.imshow(imageB, cmap = plt.cm.gray)
    #plt.axis("off")
    # show the images
    #plt.show()
    return s

def compare_images2(imageAPath, imageBPath):
    # compute the mean squared error and structural similarity
    
    response = requests.get('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7', stream=True)
    img = Image.open(response.raw)

    plt.imshow(img)
    plt.show()

def test():
    # compute the mean squared error and structural similarity
    #response = requests.get('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7')
    # This portion is part of my test code
    response = requests.get('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7')
    #img = Image.open(BytesIO(response.content))
    
    byteImgIO = io.BytesIO()
    byteImg = Image.open(response.content)
    byteImg.save(byteImgIO, "PNG")
    byteImg = byteImgIO.read()

    dataBytesIO = io.BytesIO(byteImg)
    Image.open(dataBytesIO)


    # Non test code
    dataBytesIO = io.BytesIO(byteImg)
    Image.open(dataBytesIO)
  
    #s = measure.compare_ssim(img, img, multichannel=True)
    #print(s)
    #imageB = cv2.imread(imageBPath)
    
    # setup the figure
    #fig = plt.figure(title)
    #plt.suptitle("SSIM: %.2f" % (s))
    # show first image
    #ax = fig.add_subplot(1, 2, 1)
    #plt.imshow(imageA, cmap = plt.cm.gray)
    #plt.axis("off")
    # show the second image
    #ax = fig.add_subplot(1, 2, 2)
    #plt.imshow(imageB, cmap = plt.cm.gray)
    #plt.axis("off")
    # show the images
    #plt.show()
    #return s

if __name__ == "__main__":
    a = 0
    #test()
    # imageA = cv2.imread("IMG_7162.JPG")
    # imageB = cv2.imread("black.jpg")
    # imageC = cv2.imread("white.jpg")
    #imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)  
    #imageB = imageA
    compare_images2('https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7','https://images.app.goo.gl/ymq4LeVVYF5Pq5Bi7')
