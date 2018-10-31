import numpy as np
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
img1_3D = cv2.imread('mountain_two.jpg')
img2_3D = cv2.imread('mountain_two.jpg')
img1 = cv2.imread('mountain_one.jpg',0)
img2 = cv2.imread('mountain_two.jpg',0)

# Initialization of the Feature Detector
orb = cv2.ORB_create()

# Locate keypoints in the image
kp = orb.detect(img1,None)
kp2 = orb.detect(img2,None)

# Calculate descriptors for the image
kp, desc = orb.compute(img1,kp)
kp2, desc2 = orb.compute(img2,kp2)

# Create BFMatcher object for Matching Images
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

# Match Descriptor, Similar Features between 2 Images
matches = bf.match(desc,desc2)

# Sort the matches in order of distance for sitching/meshing
matches_final = sorted(matches, key = lambda x:x.distance)

# Remove "BAD" matches (85% threshold, only keep top 15% of matches)
goodMatches = int(len(matches_final)*0.15)
matches_final = matches_final[:goodMatches]

# Draw the Keypoints in the image
img3 = cv2.drawMatches(img1,kp,img2,kp2,matches_final[:500],None,flags=2)
#plt.imshow(img3),plt.show()

# Show final Panorama of the Image
# Use RANSAC algorithm to find Homography (translation+rotation) matrix
points1 = np.zeros((len(matches),2), dtype=np.float32) # Initialization
points2 = np.zeros((len(matches),2), dtype=np.float32) # Initialization
for x, match in enumerate(matches):
    points1[x,:] = kp[match.queryIdx].pt
    points2[x,:] = kp2[match.trainIdx].pt
h_matrix, mask = cv2.findHomography(points1,points2,cv2.RANSAC)

# Method 2: Stitch of similarities + original images
# Show final Panorama of the Image
result = cv2.warpPerspective(img1,h_matrix,(img1_3D.shape[1] + img2_3D.shape[1], img1_3D.shape[0]))
result[0:img2_3D.shape[0], 0:img2_3D.shape[1]] = img2

cv2.imwrite("output2.jpg",result)


# Moving Forward - Modularize this script, implement OO Design principes
