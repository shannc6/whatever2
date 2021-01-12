# import the necessary packages
#from skimage.measure import structural_similarity as ssim
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2 

# def mse(imageA, imageB):
# 	# the 'Mean Squared Error' between the two images is the
# 	# sum of the squared difference between the two images;
# 	# NOTE: the two images must have the same dimension
# 	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
# 	err /= float(imageA.shape[0] * imageA.shape[1])
	
# 	# return the MSE, the lower the error, the more "similar"
# 	# the two images are
# 	return err

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

if __name__ == "__main__":
    a = 0
    # imageA = cv2.imread("IMG_7162.JPG")
    # imageB = cv2.imread("black.jpg")
    # imageC = cv2.imread("white.jpg")
    #imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)  
    #imageB = imageA
    # compare_images("IMG_7162.JPG", "black.", 'test')
