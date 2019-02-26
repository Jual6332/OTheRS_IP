#!/usr/bin/env python3
################################################################################
################################################################################
### ImageSlicing - "main.py" ################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/25/19   ####################################################
##  Date Modified: 2/26/19  ####################################################
################################################################################

# Main Purpose: Break up the image into representative tiles

#####################---------Libraries---------################################
import image_slicer
import numpy as np
import cv2
import math
import time
import sys
from image_slicer import join
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt
from random import randrange
##################---------Global Variables---------#############################
WIDTH = 160
HEIGHT = 120
data = numpy.zeros((HEIGHT, WIDTH))
#####################---------Main Code---------################################
def main():
    # Import Images
    bottomMount = cv2.imread('StackImages/bottomMount.png',cv2.IMREAD_COLOR) # First Image
    topMount = cv2.imread('StackImages/topMount.png',cv2.IMREAD_COLOR) # Second Image

    # Call Image_Slicer
    num_tiles = 36
    tiles = image_slicer.slice('StackImages/bottomMount.png',num_tiles, save=False)
    image_slicer.save_tiles(tiles,directory='Outputs',prefix='slice',format='png')

    # Overlay tiles
    for tile in tiles:
        overlay = ImageDraw.Draw(tile.image)
        overlay.text((5,5),str(tile.number),(255,255,255),ImageFont.load_default())
    image_slicer.save_tiles(tiles,directory='Outputs/NumberedTiles',prefix='slice',format='png')
    #image_slicer.save_tiles(tiles,directory='Outputs',prefix='slice',format='png')
    image = join(tiles)
    image.save('watch-join.png')

    #write_image("Outputs/bottomMount",bottomMount) # Write Full Image

def load_temp_values():


def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
