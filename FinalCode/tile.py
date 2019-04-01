#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "tile.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/26/19   ####################################################
##  Date Modified: 3/31/19  ####################################################
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
from statistics import mean
from random import randrange
##################---------Global Variables---------############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
#####################---------Main Code---------################################

# Function: Load Temp Values from FLIR output txt files
# Input:
# Output:
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
    data_left = load_temp_values('Inputs/March24GridTest/raw1.txt')/100 - 273.15
    data_right = load_temp_values('Inputs/March24GridTest/raw2.txt')/100 - 273.15
    tiles_left = load_grid_data('left')
    tiles_right = load_grid_data('right')

    ## Left Tiles
    # Tile 2
    temp_data = []
    for i in range(0,len(tiles_left["tile2"]["coordinatesX"])):
        x = tiles_left["tile2"]["coordinatesX"][i]
        y = tiles_left["tile2"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile2"]["tempdata"] = temp_data
    tiles_left["tile2"]["meantemp"] = mean(temp_data)
    tiles_left["tile2"]["maxtemp"] = 10
    tiles_left["tile2"]["mintemp"] = 0

    # Tile 3
    temp_data = []
    for i in range(0,len(tiles_left["tile3"]["coordinatesX"])):
        x = tiles_left["tile3"]["coordinatesX"][i]
        y = tiles_left["tile3"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile3"]["tempdata"] = temp_data
    tiles_left["tile3"]["meantemp"] = mean(temp_data)
    tiles_left["tile3"]["maxtemp"] = 10
    tiles_left["tile3"]["mintemp"] = 0

    # Tile 4
    temp_data = []
    for i in range(0,len(tiles_right["tile4"]["coordinatesX"])):
        x = tiles_right["tile4"]["coordinatesX"][i]
        y = tiles_right["tile4"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile4"]["tempdata"] = temp_data
    tiles_right["tile4"]["meantemp"] = mean(temp_data)
    tiles_right["tile4"]["maxtemp"] = 10
    tiles_right["tile4"]["mintemp"] = 0

    # Tile 5
    temp_data = []
    for i in range(0,len(tiles_right["tile5"]["coordinatesX"])):
        x = tiles_right["tile5"]["coordinatesX"][i]
        y = tiles_right["tile5"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile5"]["tempdata"] = temp_data
    tiles_right["tile5"]["meantemp"] = mean(temp_data)
    tiles_right["tile5"]["maxtemp"] = 10
    tiles_right["tile5"]["mintemp"] = 0

    # Tile 7
    temp_data = []
    for i in range(0,len(tiles_left["tile7"]["coordinatesX"])):
        x = tiles_left["tile7"]["coordinatesX"][i]
        y = tiles_left["tile7"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile7"]["tempdata"] = temp_data
    tiles_left["tile7"]["meantemp"] = mean(temp_data)
    tiles_left["tile7"]["maxtemp"] = 10
    tiles_left["tile7"]["mintemp"] = 0

    # Tile 8
    temp_data = []
    for i in range(0,len(tiles_left["tile8"]["coordinatesX"])):
        x = tiles_left["tile8"]["coordinatesX"][i]
        y = tiles_left["tile8"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile8"]["tempdata"] = temp_data
    tiles_left["tile8"]["meantemp"] = mean(temp_data)
    tiles_left["tile8"]["maxtemp"] = 10
    tiles_left["tile8"]["mintemp"] = 0

    # Tile 9
    temp_data = []
    for i in range(0,len(tiles_left["tile9"]["coordinatesX"])):
        x = tiles_left["tile9"]["coordinatesX"][i]
        y = tiles_left["tile9"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile9"]["tempdata"] = temp_data
    tiles_left["tile9"]["meantemp"] = mean(temp_data)
    tiles_left["tile9"]["maxtemp"] = 10
    tiles_left["tile9"]["mintemp"] = 0

    # Tile 10
    temp_data = []
    for i in range(0,len(tiles_right["tile10"]["coordinatesX"])):
        x = tiles_right["tile10"]["coordinatesX"][i]
        y = tiles_right["tile10"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile10"]["tempdata"] = temp_data
    tiles_right["tile10"]["meantemp"] = mean(temp_data)
    tiles_right["tile10"]["maxtemp"] = 10
    tiles_right["tile10"]["mintemp"] = 0

    # Tile 11
    temp_data = []
    for i in range(0,len(tiles_right["tile11"]["coordinatesX"])):
        x = tiles_right["tile11"]["coordinatesX"][i]
        y = tiles_right["tile11"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile11"]["tempdata"] = temp_data
    tiles_right["tile11"]["meantemp"] = mean(temp_data)
    tiles_right["tile11"]["maxtemp"] = 10
    tiles_right["tile11"]["mintemp"] = 0

    # Tile 12
    temp_data = []
    for i in range(0,len(tiles_right["tile12"]["coordinatesX"])):
        x = tiles_right["tile12"]["coordinatesX"][i]
        y = tiles_right["tile12"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile12"]["tempdata"] = temp_data
    tiles_right["tile12"]["meantemp"] = mean(temp_data)
    tiles_right["tile12"]["maxtemp"] = 10
    tiles_right["tile12"]["mintemp"] = 0

    ## Define Trays
    # Define Tray 1
    tray1 = {}
    tray1["tile2"] = tiles_left["tile2"]
    tray1["tile3"] = tiles_left["tile3"]
    tray1["tile4"] = tiles_right["tile4"]
    tray1["tile5"] = tiles_right["tile5"]
    print(tray1["tile2"]["meantemp"])
    print(tray1["tile3"]["meantemp"])
    print(tray1["tile4"]["meantemp"])
    print(tray1["tile5"]["meantemp"])
    # Define Tray 2
    tray2 = {}
    tray2["tile7"] = tiles_left["tile7"]
    tray2["tile8"] = tiles_left["tile8"]
    tray2["tile9"] = tiles_left["tile9"]
    tray2["tile10"] = tiles_right["tile10"]
    tray2["tile11"] = tiles_right["tile11"]
    tray2["tile12"] = tiles_right["tile12"]
    print(tray2["tile7"]["meantemp"])
    print(tray2["tile8"]["meantemp"])
    print(tray2["tile9"]["meantemp"])
    print(tray2["tile10"]["meantemp"])
    print(tray2["tile11"]["meantemp"])
    print(tray2["tile12"]["meantemp"])
    # Define Tray 3
    tray3 = {}

# Function: Load Grid Data from External CSV files for each image
# Input:
# Output:
def load_grid_data(side):
    tiles={}
    left_range = [2,3,7,8,9,13,14,15,19,20,21,25,26,27,32,33]
    right_range = [4,5,10,11,12,16,17,18,22,23,24,28,29,30,34,35]
    #index_left = [2,3,7,8,9]
    #index_right = [4,5,10,11,12]
    if side == "left":
        for i in left_range:
            filename = 'ImageJData/Left/tile'+str(i)+'.csv'
            coordinates = load_tile_data(filename)
            tiles["tile"+str(i)] = {"coordinatesX":coordinates[:][0],"coordinatesY":coordinates[:][1]}
    elif side == "right":
        for i in right_range:
            filename = 'ImageJData/Left/tile'+str(i)+'.csv'
            coordinates = load_tile_data(filename)
            tiles["tile"+str(i)] = {"coordinatesX":coordinates[:][0],"coordinatesY":coordinates[:][1]}
    return(tiles)

# Function: Load Temp Data for tiles in each image
# Input:
# Output:
def load_tile_data(filename):
    df = pd.read_csv(filename)
    x_column = df['X']
    y_column = df['Y']
    tile=[]
    tile.append(x_column)
    tile.append(y_column)
    return(tile)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
