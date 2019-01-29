#!/usr/bin/python3
import math
import cv2
import time
import imutils
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as pylepton

# Load Image
def load_image(name):
    img = cv2.imread(name)
    return(img)

def kmeans(img,Z,K):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret, label, center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return(res2)

def main():
    img = load_image('bulb.png')
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    output = kmeans(img,Z,8)
    cv2.imwrite('test1.png',output)

if __name__ == "__main__":
    runtime = main() # Functionality
