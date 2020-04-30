#Imports the print function from newer versions of python
from __future__ import print_function
#Setup
# The Random module for implements pseudo-random number generators
import random
# Numpy is the main package for scientific computing with Python.
# This will be one of our most used libraries in this class
import numpy as np
#Imports all the methods in each of the files: linalg.py and imageManip.py
from linalg import *
from imageManip import *
#Matplotlib is a useful plotting library for python
import matplotlib.pyplot as plt
from skimage import color,io


image1_path = './image1.jpg'
image2_path = './image2.jpg'

def display(img):
    # Show image
    plt.figure(figsize = (5,5))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

image1 = load(image1_path)
image2 = load(image2_path)
image1 = image1.astype(np.float64) / 255
image1=color.rgb2grey(image1)

lab = color.rgb2lab(image1)
out = None

### YOUR CODE HERE
a = {'L': [1, 2], 'A': [0, 2], 'B': [0, 1]}
out = np.zeros(image.shape)
out[:, :, a[channel]] = image[:, :, a[channel]]

display(image1)
display(image2)