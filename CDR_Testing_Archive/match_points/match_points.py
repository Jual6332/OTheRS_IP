#!/usr/bin/env python3

##
# A simple example of taking two images and finding the common points between them
##
import sys
import cv2
import numpy
from   matplotlib import pyplot as plt

# OpenCV loads into BGR colorspace but pyplot works in RGB
def bgr2rgb(img):
    b, g, r = cv2.split(img)
    return cv2.merge([r, g, b])

# default images
if len(sys.argv) < 3:
    img1_path = "mountain_one.jpg"
    img2_path = "mountain_two.jpg"
else:
    img1_path = sys.argv[1]
    img2_path = sys.argv[2]

img1 = bgr2rgb(cv2.imread(img1_path))
img2 = bgr2rgb(cv2.imread(img2_path))

# BRISK detector instead of ORB
brisk = cv2.BRISK_create()
kp1, desc1 = brisk.detectAndCompute(img1, None)
kp2, desc2 = brisk.detectAndCompute(img2, None)
# print("# kps: {}, descriptors: {}".format(len(kp1), desc1.shape))
# print("# kps: {}, descriptors: {}".format(len(kp2), desc2.shape))

# Brute force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(desc1, desc2)
matches = sorted(matches, key = lambda x: x.distance)
# print("{} matches".format(len(matches)))

points1 = numpy.zeros((len(matches), 2), dtype=numpy.float32)
points2 = numpy.zeros((len(matches), 2), dtype=numpy.float32)

for x, match in enumerate(matches):
    points1[x, :] = (kp1[match.queryIdx].pt)
    points2[x, :] = (kp2[match.queryIdx].pt)

h_matrix, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
# print(h_matrix)

# result1 = cv2.warpPerspective(img1, h_matrix, (img1.shape[1], img1.shape[0]))
# result2 = cv2.warpPerspective(img2, h_matrix, (img2.shape[1], img2.shape[0]))
# plt.imshow(result2)

# Draw where the images match
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=2)
plt.imshow(img3)
plt.show()

