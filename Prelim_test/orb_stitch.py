#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
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

def alignImages(img1,img2):
    # Convert Images to Grayscale
    img1Gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2Gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

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

    # Remove "BAD" matches (85% threshold, only keep top 15% of matches)
    goodMatches = int(len(matches_final)*0.15)
    matches_final = matches_final[:goodMatches]

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

    # Find Homography Matrix
    h_matrix, mask = cv2.findHomography(points1,points2,cv2.RANSAC,5.0)

    # Image Dimensions
    h1,w1,c1 = img1.shape
    h2,w2,c2 = img2.shape

    # Get the Canvas Dimensions
    img1_dims = np.float32([[0,0],[0,w1],[h1,w1],[h1,0]]).reshape(-1,1,2)
    img2_dims_temp = np.float32([[0,0],[0,w2],[h2,w2],[h2,0]]).reshape(-1,1,2)

    # Get Relative Perspective of second Image
    img2_dims = cv2.perspectiveTransform(img2_dims_temp,h_matrix)

    # Resulting Dimensions
    result_dims = np.concatenate((img1_dims,img2_dims),axis=0)

    # Calculating dimensions of matched points
    [x_min,y_min] = np.int32(result_dims.min(axis=0).ravel()-0.5)
    [x_max,y_max] = np.int32(result_dims.max(axis=0).ravel()+0.5)

    # Create Output Array after
    transform_dist = [-x_min,-y_min]
    transform_array = np.array([[1,0,transform_dist[0]],[0,1,transform_dist[1]],[0,0,1]])

    # Warp Images to get the Resulting Image
    result_img = cv2.warpPerspective(img2,transform_array.dot(h_matrix),(x_max-x_min,y_max-y_min))
    A = img1.shape[1]
    B = img1.shape[0]

    stitcher = cv2.createStitcher(False)
    result = stitcher.stitch((img1,img2))
    cv2.imwrite("output2.jpg",result[1])

    # Display First Image
    plt.imshow(img1)
    plt.title('Input Image A')
    plt.show(); plt.figure()

    # Display Second Image
    plt.imshow(img2)
    plt.title('Input Image B')
    plt.show(); plt.figure()

    # Save Image
    plt.imshow(result[1])
    plt.title('Warped Image')
    plt.show(); plt.figure()

    return result, h_matrix

if __name__ == '__main__':
    # Read in images
    img = cv2.imread('mountain_one.jpg',cv2.IMREAD_COLOR) # Left image for stitch
    img2 = cv2.imread('mountain_two.jpg',cv2.IMREAD_COLOR) # Right image for stitch
    #stitcher = cv2.createStitcher()
    #images = []; images.append(img); images.append(img2)
    #ret, pano = stitcher.stitch(images)
    #if ret == cv2.STITCHER_OK:
    #    cv2.imshow('panorama',pano)
    #    cv2.waitKey()
    alignImages(img,img2)
