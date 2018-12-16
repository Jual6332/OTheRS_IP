#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
from matplotlib import pyplot as plt
from random import randrange

# Read in images
img_ = cv2.imread('mountain_two.jpg') # Right image for stitch
img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY) # Grayscale 

img = cv2.imread('mountain_two.jpg') # Left image for stitch
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Grayscale
