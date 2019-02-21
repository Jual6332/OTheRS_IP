#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
import sys
from PIL import Image
from matplotlib import pyplot as plt
from random import randrange

################################################################################
### "run_stitchAPI.py" #########################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 1/20/19   ####################################################
##  Date Modified: 2/16/19  ####################################################
################################################################################

# Main Purpose: Continue to explore image stitching techniques. Return StitchAPI
# resulting image data.

# Action Item: Test with

# Caution: Prevent temperature data from being compromised.

#####################---------Main Code---------################################
def main():
    # Read in images
    img = cv2.imread('Inputs/stitch3.png',cv2.IMREAD_COLOR) # Left image for stitch
    img2 = cv2.imread('Inputs/stitch4.png',cv2.IMREAD_COLOR) # Right image for stitch
    align_images(img,img2) # Run Align Images
    result = call_stitchAPI(img1,img2)
    return result

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

def align_images(img1,img2):
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

    # Initialize Image Objects
    points1 = np.zeros((len(matches),2), dtype=np.float32) # Initialization
    points2 = np.zeros((len(matches),2), dtype=np.float32) # Initialization

    # Extract Location of Good Matches
    for x, match in enumerate(matches):
        points1[x,:] = kp[match.queryIdx].pt
        points2[x,:] = kp2[match.trainIdx].pt

def call_stitchAPI(img1,img2):
    # Call Stitch API, return resulting image data
    stitcher = cv2.createStitcher(False)
    result = stitcher.stitch((img1,img2))
    return result[1]

if __name__ == '__main__':
    cv2.imwrite("Outputs/Low-ResThermalOutput.jpg",result) # Write Output
