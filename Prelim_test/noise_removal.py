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

# Noise Removal
def noise_removal(img1,img2):
    img_new = img1-img2 # Difference
    return(img_new)

def main():
    img2 = load_image('FLIR_first.jpg')
    img_subtract2 = load_image('FLIR_first.jpg')
    img2 = noise_removal(img2,img_subtract2)
    cv2.imwrite("Noise Removed.png",img2)

if __name__ == "__main__":
    runtime = main() # Functionality
