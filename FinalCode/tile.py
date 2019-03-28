#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "tile.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/26/19   #####################################################
##  Date Modified: 3/28/19  ####################################################
################################################################################
# Main Purpose: Break up the image into representative tiles, check temp values
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
#####################---------Main Code---------################################


## Load Temp Values and Write to Image
def load_temp_values(filename):
    # Parse file of floating point numbers into 2D array
    with open(filename, "r") as f:
        row = 0
        for line in f.read().strip().split("\n"):
            try:
                numbers = [float(i) for i in line.strip().split(" ")]
                data[row, :] = numbers
            except Exception as e:
                print("Exception: {}".format(e))
            row += 1
    ## Show, Save the result
    fig = plt.figure(frameon=False)
    ax = plt.subplot(111)
    #ax = plt.Axes(fig,[0,0,1,1])
    ax.set_axis_off()
    plt.imshow(data)
    plt.axis('off')
    fig.tight_layout()
    fig.savefig("output.png",pad_inches=0,bbox_inches='tight')
    return data

def main():
    data = load_temp_values('Inputs/March24GridTest/raw1.txt')/100 - 273.15
    print(len(data[0]))
    print(len(data))
    print(data)
    tiles_left = load_grid_data('left')
    tiles_right = load_grid_data('right')

def load_grid_data(side):
    tiles=[]
    if side == 'left':
        for i in range(2,37):
            filename = 'ImageJData/Left/tile'+str(i)+'.csv'
            tile = load_tile_data(filename)
            tiles.append(tile)
    elif side == 'right':
        for i in range(1,6):
            filename = 'ImageJData/Right/tile'+str(i)+'.csv'
            tile = load_tile_data(filename)
            tiles.append(tile)
        for i in range(7,37):
            filename = 'ImageJData/Right/tile'+str(i)+'.csv'
            tile = load_tile_data(filename)
            tiles.append(tile)
    return(tiles)


def load_tile_data(filename):
    df = pd.read_csv(filename)
    x_column = df['X']
    y_column = df['Y']
    tile=[]
    for idx in range(0,len(x_column)):
        tile.append((x_column[idx],y_column[idx]))
    return(tile)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
