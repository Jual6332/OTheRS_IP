#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
import sys
from PIL import Image
from matplotlib import pyplot as plt
from random import randrange

# Function Descriptions
def transpose(array):
    array = array[:]
    n = len(array)
    for i, row in enumerate(array):
        array[i] = row + [None for _ in range(n-len(row))]
    array = zip(*array)
    for i, row in enumerate(array):
        array[i] = [elem for elem in row if elem is not None]
    return array

# Grayscale
def gray_scale(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return(gray)

# Load Image
def load_image(name):
    img = cv2.imread(name)
    return(img)

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)

def alignImages(img1,img2):
    # Otsu Thresholding Test 1
    img1Gray = gray_scale(img1)
    thr = Otsu_thresholding(img1Gray)

    # Otsu Thresholding Test 2
    img2Gray = gray_scale(img2)
    thr2 = Otsu_thresholding(img2Gray)

    # Initialization of the Feature Detector
    orb = cv2.ORB_create()

    # Locate keypoints in the image, calculate descriptors
    kp, desc = orb.detectAndCompute(img1Gray,None)
    kp2, desc2 = orb.detectAndCompute(img2Gray,None)

    # Create BFMatcher object for Matching Images, Brutte Force Hamming Matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

    # Match Descriptor, Similar Features between 2 Images
    matches = bf.match(desc,desc2)

    # Sort the matches by score for sitching/meshing
    matches_final = sorted(matches, key = lambda x:x.distance)
    print("Total matches:"+str(len(matches_final)))

    # Remove "BAD" matches (85% threshold, only keep top 15% of matches)
    goodMatches = int(len(matches_final)*0.90)
    matches_final = matches_final[:goodMatches]
    print("Top matches:"+str(len(matches_final)))

    # Draw the top Matches in the Image
    img3 = cv2.drawMatches(img1,kp,img2,kp2,matches_final,None,flags=2)
    cv2.imwrite("output3.jpg",img3)

    # Show final Panorama of the Image
    # Use RANSAC algorithm to find Homography (translation+rotation) matrix

    # Initialize Image Objects
    points1 = np.zeros((len(matches),2), dtype=np.float32) # Initialization
    points2 = np.zeros((len(matches),2), dtype=np.float32) # Initialization

    # Extract Location of Good Matches
    for x, match in enumerate(matches):
        points1[x,:] = kp[match.queryIdx].pt
        points2[x,:] = kp2[match.trainIdx].pt

    # Call Stitch API
    stitcher = cv2.createStitcher(False)
    result = stitcher.stitch((img1,img2))
    print(result)
    #cv2.imwrite("Low-ResThermalOutput.jpg",result[1])

    ## Custom Hard-Code Solution
    # Step 1. Draw bounds for Overlapped Region
    for height_elem in range(0,img1.shape[0]):
      img1[height_elem][42][:] = 255;
      img1[height_elem][img1.shape[1]-1][:] = 255;

    # Step 2. Mask Overlapped Region
    for length_elem in range(43,img1.shape[1]-1):
      img1[0][length_elem][:] = 255;
      img1[img1.shape[0]-1][length_elem][:] = 255;

    # Step 3. Write Image - Find overlap line
    cv2.imwrite("OverlappedImage.png",img1)

    # Step 4: Find dimensions of final image
    height_overlap = img1.shape[0]
    length_overlap = 42

    print("Final height:"+str(height_overlap))
    print("Final length:"+str(length_overlap))

    # Step 5: Map Image Panorama - First Image
    img_final = np.zeros((height_overlap,length_overlap,3));
    print(img_final.shape)
    for height_elem in range(0,img1.shape[0]):
      for length_elem in range(0,42):
          img_final[height_elem][length_elem] = img1[height_elem][length_elem]

    # Step 6: Write First Image to PNG
    cv2.imwrite("FirstImage.png",img_final)


if __name__ == '__main__':
    # Read in images
    img = cv2.imread('Inputs/stitch3.png',cv2.IMREAD_COLOR) # Left image for stitch
    img2 = cv2.imread('Inputs/stitch4.png',cv2.IMREAD_COLOR) # Right image for stitch
    alignImages(img,img2)
