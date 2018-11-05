#!/usr/bin/env python3
import numpy as np
import math
import time
import cv2
from matplotlib import pyplot as plt

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
    img = load_image('IR_0561.jpg')
    gray = gray_scale(img)
    cv2.imwrite('Grayscale.png',gray)
    blur = Gaussian_blur(gray)
    ad = adaptive_thresholding(gray)
    cv2.imwrite('Adaptive Thresh.png',ad)
    ad = adaptive_thresholding(blur)
    cv2.imwrite('Adaptive Thresh + Gaussian.png',ad)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)
    file = np.float32(gray)
    dst = cv2.cornerHarris(file,2,3,0.04)
    dst = cv2.dilate(dst,None)
    cv2.imwrite('Corner Harris.png',dst)
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
