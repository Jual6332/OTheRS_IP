#!/usr/bin/env python3
import numpy
import cv2
import math
import time
import sys
from   matplotlib import pyplot as plt

# Read images from command line if available or use defaults
images = sys.argv[1:]
if len(images) < 2:
    print("Using default images")
    images = ["IMG_20181029_121916.jpg", "IMG_20181029_121919.jpg"]

# Initialization of the Feature Detector
orb = cv2.ORB_create()

for image in images:
    ## ORB Implementation - The Algorithm in Action
    # Read in image
    img = cv2.imread(image, 0)

    # Locate keypoints in the image
    kp = orb.detect(img, None)

    # Calculate descriptors for the image
    kp, desc = orb.compute(img, kp)

    # Draw the Keypoints in the image
    plt.imshow(
        cv2.drawKeypoints(img, kp, None, color = (0, 0, 255), flags = 0)
    )
    plt.show()
