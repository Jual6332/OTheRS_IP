#!/usr/bin/python3
import math
import cv2
import time
import imutils
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as pylepton

# Adaptive Thresholding
def adaptive_thresholding(img):
    ad = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    return(ad)

# Find Contours
def contours(img):
    ret, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    cv2.bitwise_not(thresh,thresh)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key=cv2.contourArea)
    left = tuple(c[c[:,:,0].argmin()][0])
    right = tuple(c[c[:,:,0].argmax()][0])
    distance = np.sqrt((right[0] - left[0])**2 + (right[1] - left[1])**2)
    [x,y,w,h] = cv2.boundingRect(c)
    centx = np.sqrt(((right[0]+left[0])**2)/4)
    centy = np.sqrt(((right[1]+left[1])**2)/4)
    return(distance,x,y,w,h,c,left,right,centx,centy)

# Guassian Thresholding
def gaussian_thresholding(img):
    ad = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return(ad)

# Gaussian Blur
def Gaussian_blur(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return(blur)

# Grayscale
def gray_scale(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return(gray)

# Geometric Calibration Functionality


#getPerspectiveTransform
#warpPerspectivd

# K-Means
def kmeans(img,Z,K):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret, label, center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return(res2)

# Load Image
def load_image(name):
    img = cv2.imread(name)
    return(img)

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)

# ORB Stitching
def orb_stitch(img1,img2):
    # Initialization of the Feature Detector
    orb = cv2.ORB_create()
    # Locate keypoints in the image
    kp = orb.detect(img1)
    kp2 = orb.detect(img2)
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
    img3 = cv2.drawMatches(img1,kp,img2,kp2,matches_final[:],None,flags=2)

# Noise Removal
def noise_removal(img1,img2):
    img_new = img1-img2 # Difference
    return(img_new)

# Remove Glare
def remove_glare(img):
    # Create CLAHE object
    clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
    # Apply CLAHE to lightness channel
    cl1 = clahe.apply(img)
    return(cl1)

def skew_transforn(img):
    rows, cols, ch = img.shape
    pts1 = np.float32([[cols*.25, rows*.95],[cols*.90,rows*.95],[cols*.1, 0],[cols, 0]])
    pts2 = np.float32([[cols*0.1, rows],[cols,rows],[0,0],[cols, 0]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(cols,rows))
    return(dst)

def main():
    start = time.time()
    # Image 1
    img = load_image('cars.jpg')
    img_subtract = load_image('FLIR_first.jpg')
    #img = noise_removal(img,img_subtract)
    img = gray_scale(img)
    img = remove_glare(img)
    cv2.imwrite('Removing Glare.png',img)

    # Image 2
    img2 = load_image('FLIR_second.jpg')
    img_subtract2 = load_image('FLIR_second.jpg')
    img2 = noise_removal(img2,img_subtract2)

    # Clean up the image
    img = load_image('FLIR_first.jpg')
    gray = gray_scale(img)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)

    # K-Means Color Quantization Test 1
    img = load_image('FLIR_first.jpg')
    img = load_image('FLIR0014.jpg')
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    output = kmeans(img,Z,8)
    cv2.imwrite('res2.png',output)

    # K-Means Color Quantization Test 2
    img = load_image('bulb.png')
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    output = kmeans(img,Z,8)
    cv2.imwrite('test1.png',output)

    # Potential Skew Angle Fix
    img = cv2.imread('box.jpg')
    dst = skew_transforn(img)
    cv2.imwrite('Skew Transform.png',dst)
    # ---> Apply Thresholding
    gray = gray_scale(dst)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Skew Transform + Otsu.png',thr)

    # Test Contours - Under Construction
    #img = load_image('bulb.png')
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #[distance,x,y,w,h,c,left,right,centx,centy] = contours(gray)
    #cv2.circle(img,left,5,(0,0,255),-1)
    #cv2.circle(img,right,5,(0,0,255),-1)
    #cv2.circle(img,(int(centx),int(centy)),5,(0,0,255),-1)
    #cv2.line(img,left,right,(255,0,0),2)
    #cv2.drawContours(img,[c],-1,(0,255,0),2)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imwrite('BulbResult.png',img)

if __name__ == "__main__":
    runtime = main() # Functionality
