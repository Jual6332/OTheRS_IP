#!/usr/bin/env python3
################################################################################
################################################################################
### Image Stitching - "stitch.py" ##############################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/8/19    ####################################################
##  Date Modified: 3/29/19  ####################################################
################################################################################
# Main Purpose: Stitch two images together
#####################---------Libraries---------################################
import pandas as pd
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
from random import randrange
##################---------Global Variables---------############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
stitched_image = []
#####################---------Main Code---------################################
# Main Function
def main():
    stitch_left_load = load_stitch_data('ImageJData/stack_face_left.csv')
    stitch_right_load = load_stitch_data('ImageJData/stack_face_right.csv')

    image_left_load = load_image('Inputs/March24GridTest/rgb1.png')
    image_right_load = load_image('Inputs/March24GridTest/rgb2.png')

    image_left_rotate = ndimage.rotate(image_left_load, -90)
    image_right_rotate = ndimage.rotate(image_right_load, 90)
    cv2.imwrite('Outputs/Left.png',image_left_rotate)
    cv2.imwrite('Outputs/Right.png',image_right_rotate)

    print(stitch_left_load[0][0])
    print(stitch_left_load[0][1])

    plt.scatter(*zip(*stitch_left_load))
    plt.show()



    """
    for j in range(0,len(image_left_load[0])):
        idx=0
        for i in range(0,len(image_left_load)):
            check = (i,j)
            if check in stitch_left_load:
                num+=1
                #print("Success!")
    """

    #print("Final="+str(num))


def load_image(name):
    img = cv2.imread(name)
    return(img)

def load_stitch_data(filename):
    df = pd.read_csv(filename)
    x_column = df['X']
    y_column = df['Y']
    #print(type(y_column[0]))
    #max(y_column,key="len")
    stitch=[]
    for idx in range(0,len(x_column)):
        stitch.append((y_column[idx],x_column[idx]))
    #print(type(stitch[0][0]))
    return(stitch)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
