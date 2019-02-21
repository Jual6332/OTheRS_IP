#!/usr/bin/env python3
################################################################################
################################################################################
### RETIRED_StitchAPI - "main.py" ##############################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 1/28/19   ####################################################
##  Date Modified: 2/16/19  ####################################################
################################################################################

# Main Purpose: Continue to explore image stitching techniques. Return StitchAPI
# resulting image data. Accept two camera images and write final stitch
# Action Item: Test with 160X120 images.
# Caution: Prevent temperature data from being compromised.

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
    # Step 6: Write First Image to PNG
    #cv2.imwrite("FirstImage.png",img_final)
    # Step 7: Concatenate Images
    image_first = cv2.imread('Inputs/FirstImage.png',cv2.IMREAD_COLOR) # First Image
    image_second = cv2.imread('Inputs/stitch4.png',cv2.IMREAD_COLOR) # Second Image
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
