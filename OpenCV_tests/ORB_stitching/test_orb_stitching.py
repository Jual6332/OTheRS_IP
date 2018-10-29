import numpy
import cv2
import math
from matplotlib import pyplot as plt

## Date Last Modified: 10/28/18
# Justin Alvey

## Purpose: To test the ORB stitchiing strategy available through the OpenCV library

# ORB is an efficient alternative to SIFT or SURF, both in computation cost, performance
# in locating image feature similarities, and since it has no patents.

# ORB Features:
# 1.) cv2.ORB_create() - Constructor
# 2.) orb.detect(img, None) - Locate the high-variance locations in the image
# 3.) orb.compute(img, keypoints) - Computes Descriptors or the pixel intensity comparisons
#     BRIEF - Binary Robust Independent Elementary Features ...
#     ORB builds on this heritage of feature matching called FAST and BRIEF

## ORB Implementation - The Algorithm in Action
# Read in first image
img = cv2.imread('mountain_one.jpg',0)

# Initialization of the Feature Detector
orb = cv2.ORB_create()

# Locate keypoints in the image
kp = orb.detect(img, None)

# Calculate descriptors for the image
kp, desc = orb.compute(img, kp)

# Draw the Keypoints in the image
img2 = cv2.drawKeypoints(img, kp, None, color = (0, 0, 255), flags = 0)
plt.imshow(img2)
plt.show()
