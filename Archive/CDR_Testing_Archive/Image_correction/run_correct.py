#!/usr/bin/env python3
import numpy as np
import math
import time
import cv2
from matplotlib import pyplot as plt

def gaussian_thresholding(img):
    ad = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return(ad)

def Gaussian_blur(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return(blur)

def gray_scale(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return(gray)

def load_image(name):
    img = cv2.imread(name)
    return(img)

def adaptive_thresholding(img):
    ad = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    return(ad)

def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)
    # retval is not really needed, not used here.

def main():
    start = time.time()
    #img = load_image('IR_0560.jpg')
    #img = load_image('thermal2.jpg')
    img = load_image('chessboard.jpg')
    gray = gray_scale(img)
    cv2.imwrite('Grayscale.png',gray)
    blur = Gaussian_blur(gray)
    ad = gaussian_thresholding(blur)
    cv2.imwrite('Gaussian Thresh.png',ad)
    ad = adaptive_thresholding(gray)
    cv2.imwrite('Adaptive Thresh.png',ad)
    ad = adaptive_thresholding(blur)
    cv2.imwrite('Adaptive Thresh + Gaussian.png',ad)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)
    gray = np.float32(gray)
    # Corner Harris does not look useful
    # Scheme -> Restrict exposure in the image to temp. cold/hot-spots
    #        -> Locate these geometric shapes in the image using contours
    #        -> Identify the tray elements
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    img[dst>0.01*dst.max()] = [0,0,255]
    cv2.imwrite('Corner Harris.png',img)
    end = time.time()
    return(end-start)

if __name__ == "__main__":
    running_times=[] # Running times, for 100 sims
    for i in range(0,100):
        runtime = main() # Functionality
        running_times.append(runtime)
    print(runtime)
    # Average of 50 simulations
    print("Avg run-time is: "+str(1000*np.mean(running_times,dtype=np.float32))+" ms.")
