#!/usr/bin/env python3
import numpy
import cv2
import math
import time
import sys
from matplotlib import pyplot as plt

images = sys.argv[1:]
if len(images) < 2:
    print("Add more args")
    sys.exit(1)


for image in images:
    ## ORB Implementation - The Algorithm in Action
    # Read in first image
    img = cv2.imread(image, 0)

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
