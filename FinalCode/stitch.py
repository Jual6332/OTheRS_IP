#!/usr/bin/env python3
################################################################################
################################################################################
### Image Stitching - "stitch.py" ##########################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/8/19   #####################################################
##  Date Modified: 4/16/19  #####################################################
################################################################################
# Main Purpose: Final stitch for two images together
#####################---------Libraries---------################################
import image_slicer
import numpy as np
import cv2
import math
import PIL
import time
import sys
from image_slicer import join
from PIL import Image, ImageDraw, ImageFont, ImageChops
from matplotlib import pyplot as plt
from scipy import ndimage
from statistics import mean
from random import randrange
##################---------Global Variables---------############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
stitched_image = []
#####################---------Main Code---------################################
# Main Function
def main():
    Test1(); # Test 1

# Unit Test 1
def Test1():
    # Load Images
    fName_left = "Inputs/March24GridTest/"+str(sys.argv[1])+"/image1"
    fName_right = "Inputs/March24GridTest/"+str(sys.argv[1])+"/image2"
    image_left = np.loadtxt(fName_left)
    image_right = np.loadtxt(fName_right)
    
    # Save Image in PNG form
    img = Image.fromarray(image_left,'RGB')
    img.save('Outputs/Image_left.png')
    img.show()
    img = Image.fromarray(image_right,'RGB')
    img.save('Outputs/Image_right.png')
    img.show()
    print(image_left)
    write_image("Outputs/Image1.png",image_left)
    
    # Rotate Images
    left_stack_select = select_stack_data_left(image_left) # Locate Stack
    right_stack_select = select_stack_data_right(image_right) # Locate Stack
    #write_image("Outputs/left_image1",left_stack_select)
    #write_image("Outputs/right_image1",right_stack_select)

    left = ndimage.rotate(left_stack_select, -90) # Rotate stack image CW 90deg
    right = ndimage.rotate(right_stack_select, 90) # Rotate stack image CCW 90deg

    # Concatenate Images
    stitched_image = concatenate_images(left,right)
    #write_image("Outputs/left_image",left)
    #write_image("Outputs/right_image",right)
    write_image("Outputs/stitched_image",stitched_image) # Write Full Image

# Function: Load image data from file
# Input: Name of file as a string
# Output: Image data of size (WIDTH X HEIGHT X 3)
def concatenate_images(image_first,image_second):
    stack_image_data = np.hstack((image_first,image_second)) # Horizontally Stack Img Data
    result = np.concatenate((image_first,image_second), axis=1) # Concatenate
    return result

# Function: Load image data from file
# Input: Name of file as a string
# Output: Image data of size (WIDTH X HEIGHT X 3)
def load_image(name):
    img = cv2.imread(name)
    return(img)

# Function: Load image data from file
# Input: Name of file as a string
# Output: Image data of size (WIDTH X HEIGHT X 3)
def select_stack_data_left(img):
    empty_img = np.zeros([65,160,3])
    i=0;j=0;
    for idx in range(0,159):
        i += 1; j=0;
        for idy in range(38,102):
            j+=1;
            empty_img[j][i][:] = img[idy][idx]
    return(empty_img)

# Function: Load image data from file
# Input: Right Image data of size (WIDTH X HEIGHT X 3)
# Output: Simplified Right Image data of size (WIDTH X HEIGHT X 3)
def select_stack_data_right(img):
    empty_img = np.zeros([86,160,3])
    i=0;j=0;
    for idx in range(0,159):
        i += 1; j=0;
        for idy in range(26,111):
            j+=1;
            empty_img[j][i][:] = img[idy][idx]
    numrows = len(empty_img)
    numcols = len(empty_img[0])
    new_img = np.zeros([numrows-22,numcols,3])
    i=0;j=0;
    for idx in range(0,numcols-1):
        i+=1; j=0;
        for idy in range(23,numrows):
            j+=1;
            new_img[j][i][:] = empty_img[idy][idx]
    return(new_img)

# Function: Load image data from file
# Input: Name of file as a string
# Output: Image data of size (WIDTH X HEIGHT X 3)
def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data)

if __name__ == '__main__':
    times=[]
    for i in range(0,1):
        start = time.time()
        main()
        end = time.time()
        times.append(end-start)
    print("Mean time to complete is: "+str(mean(times))+" seconds")
#####################-----------Close-----------################################
