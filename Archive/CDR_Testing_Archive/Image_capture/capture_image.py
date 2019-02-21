#!/usr/bin/env python3
import numpy as np
import cv2
import time
from pylepton import Lepton

# Keep commented out until we can test w FLIR Lepton camera
#with Lepton() as l:
#    a,_ = l.capture()

# Sensor Data is Read-in as 14-bit, extend to 16 bits without loosing data
#test = cv2.normalize(a,a,0,65535,cv2.NORM_MINMAX)
#cv2.imwrite("output.png", np.uint16(a))

# Timing Analysis to see the O(n) running time of the algorithm
running_times = []
for i in range(0,100):
    start = time.time()
    # =================================================== #
    # Test Code, since we are not hooked up w FLIR Lepton, use this algorithm as a test
    # The part of the algorithm we really want to highlight is the section:
    # 1.) load array > 2.) normalize > 3.) write to file
    # This code below should do the trick for timing purposes for RFA
    img = cv2.imread("FLIR.jpg") # load image
    h, w, ch = img.shape
    emptyImg = np.zeros((h, w)) # Image for manipulation
    #emptyImg = cv2.GaussianBlur(img, (5,5), 0) # Apply Blur, mimic image sharpening

    # 8 bits
    normalizedImg = cv2.normalize(img, emptyImg, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite("8-bits.png", normalizedImg)

    # 16 bits
    normalizedImg = cv2.normalize(img, emptyImg, 0, 65535, cv2.NORM_MINMAX)
    cv2.imwrite("16-bits.png", normalizedImg)

    # Timing Analysis to see the O(n) running time of the algorithm
    end = time.time()

    # Store this time
    running_times.append(end-start)

# Average of 50 simulations
print("Avg run-time is: "+str(1000*np.mean(running_times,dtype=np.float32))+" ms.")
