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
import os

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
    imageA = io.imread(imageAPath) if validators.url(imageAPath) else cv2.imread(imageAPath)
    imageB = io.imread(imageBPath) if validators.url(imageBPath) else cv2.imread(imageBPath)
    s = measure.compare_ssim(imageA, imageB, multichannel=True)
    return s
