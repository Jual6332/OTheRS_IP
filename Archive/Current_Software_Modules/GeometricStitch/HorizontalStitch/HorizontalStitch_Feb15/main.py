#!/usr/bin/env python3
################################################################################
################################################################################
### Feb 15, Horizontal Stitch - "main.py" ##############################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/20/19   ####################################################
##  Date Modified: 2/28/19  ####################################################
################################################################################
# Main Purpose:
# Action Item:
# Caution:
#####################---------Libraries---------################################
import numpy as np
import cv2
import math
import time
import sys
from PIL import Image
from matplotlib import pyplot as plt
from random import randrange

#####################---------Main Code---------################################
def main():
    # Step 7: Concatenate Images
    image_first = cv2.imread('Inputs/.png',cv2.IMREAD_COLOR) # First Image
    image_second = cv2.imread('Inputs/.png',cv2.IMREAD_COLOR) # Second Image
    image_final = concatenate_images(image_first,image_second)
    # Step 8: Write Final Image
    write_image("Outputs/FinalImage",image_final) # Write Full Image

def concatenate_images(image_first,image_second):
    stack_image_data = np.hstack((image_first,image_second)) # Horizontally Stack Img Data
    result = np.concatenate((image_first,image_second), axis=1) # Concatenate
    return result

def load_image(name):
    img = cv2.imread(name)
    return(img)

def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
