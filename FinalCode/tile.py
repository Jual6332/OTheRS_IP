#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "tile.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/26/19   ####################################################
##  Date Modified: 4/5/19   ####################################################
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
    #fig = plt.figure(frameon=False)
    #ax = plt.subplot(111)
    #ax = plt.Axes(fig,[0,0,1,1])
    #ax.set_axis_off()
    #plt.imshow(data)
    #plt.axis('off')
    #fig.tight_layout()
    #fig.savefig("output.png",pad_inches=0,bbox_inches='tight')
    return data

def main():
    data_left = load_temp_values('Inputs/March24GridTest/Test1/left.txt')/100 - 273.15
    data_right = load_temp_values('Inputs/March24GridTest/Test1/right.txt')/100 - 273.15
    tiles_left = load_grid_data('left')
    tiles_right = load_grid_data('right')

    ## Left Tiles
    # Tile 2
    temp_data = []
    for i in range(0,len(tiles_left["tile2"]["coordinatesX"])):
        x = tiles_left["tile2"]["coordinatesX"][i]
        y = tiles_left["tile2"]["coordinatesY"][i]
        val = data_left[y][x]
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
        val = data_left[y][x]
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
        val = data_left[y][x]
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
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile12"]["tempdata"] = temp_data
    tiles_right["tile12"]["meantemp"] = mean(temp_data)
    tiles_right["tile12"]["maxtemp"] = 10
    tiles_right["tile12"]["mintemp"] = 0

    # Tile 13
    temp_data = []
    for i in range(0,len(tiles_left["tile13"]["coordinatesX"])):
        x = tiles_left["tile13"]["coordinatesX"][i]
        y = tiles_left["tile13"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile13"]["tempdata"] = temp_data
    tiles_left["tile13"]["meantemp"] = mean(temp_data)
    tiles_left["tile13"]["maxtemp"] = 10
    tiles_left["tile13"]["mintemp"] = 0

    # Tile 14
    temp_data = []
    for i in range(0,len(tiles_left["tile14"]["coordinatesX"])):
        x = tiles_left["tile14"]["coordinatesX"][i]
        y = tiles_left["tile14"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile14"]["tempdata"] = temp_data
    tiles_left["tile14"]["meantemp"] = mean(temp_data)
    tiles_left["tile14"]["maxtemp"] = 10
    tiles_left["tile14"]["mintemp"] = 0

    # Tile 15
    temp_data = []
    for i in range(0,len(tiles_left["tile15"]["coordinatesX"])):
        x = tiles_left["tile15"]["coordinatesX"][i]
        y = tiles_left["tile15"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile15"]["tempdata"] = temp_data
    tiles_left["tile15"]["meantemp"] = mean(temp_data)
    tiles_left["tile15"]["maxtemp"] = 10
    tiles_left["tile15"]["mintemp"] = 0

    # Tile 16
    temp_data = []
    for i in range(0,len(tiles_right["tile16"]["coordinatesX"])):
        x = tiles_right["tile16"]["coordinatesX"][i]
        y = tiles_right["tile16"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile16"]["tempdata"] = temp_data
    tiles_right["tile16"]["meantemp"] = mean(temp_data)
    tiles_right["tile16"]["maxtemp"] = 10
    tiles_right["tile16"]["mintemp"] = 0

    # Tile 17
    temp_data = []
    for i in range(0,len(tiles_right["tile17"]["coordinatesX"])):
        x = tiles_right["tile17"]["coordinatesX"][i]
        y = tiles_right["tile17"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile17"]["tempdata"] = temp_data
    tiles_right["tile17"]["meantemp"] = mean(temp_data)
    tiles_right["tile17"]["maxtemp"] = 10
    tiles_right["tile17"]["mintemp"] = 0

    # Tile 18
    temp_data = []
    for i in range(0,len(tiles_right["tile18"]["coordinatesX"])):
        x = tiles_right["tile18"]["coordinatesX"][i]
        y = tiles_right["tile18"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile18"]["tempdata"] = temp_data
    tiles_right["tile18"]["meantemp"] = mean(temp_data)
    tiles_right["tile18"]["maxtemp"] = 10
    tiles_right["tile18"]["mintemp"] = 0

    # Tile 19
    temp_data = []
    for i in range(0,len(tiles_left["tile19"]["coordinatesX"])):
        x = tiles_left["tile19"]["coordinatesX"][i]
        y = tiles_left["tile19"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile19"]["tempdata"] = temp_data
    tiles_left["tile19"]["meantemp"] = mean(temp_data)
    tiles_left["tile19"]["maxtemp"] = 10
    tiles_left["tile19"]["mintemp"] = 0

    # Tile 20
    temp_data = []
    for i in range(0,len(tiles_left["tile20"]["coordinatesX"])):
        x = tiles_left["tile20"]["coordinatesX"][i]
        y = tiles_left["tile20"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile20"]["tempdata"] = temp_data
    tiles_left["tile20"]["meantemp"] = mean(temp_data)
    tiles_left["tile20"]["maxtemp"] = 10
    tiles_left["tile20"]["mintemp"] = 0

    # Tile 21
    temp_data = []
    for i in range(0,len(tiles_left["tile21"]["coordinatesX"])):
        x = tiles_left["tile21"]["coordinatesX"][i]
        y = tiles_left["tile21"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile21"]["tempdata"] = temp_data
    tiles_left["tile21"]["meantemp"] = mean(temp_data)
    tiles_left["tile21"]["maxtemp"] = 10
    tiles_left["tile21"]["mintemp"] = 0

    # Tile 22
    temp_data = []
    for i in range(0,len(tiles_right["tile22"]["coordinatesX"])):
        x = tiles_right["tile22"]["coordinatesX"][i]
        y = tiles_right["tile22"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile22"]["tempdata"] = temp_data
    tiles_right["tile22"]["meantemp"] = mean(temp_data)
    tiles_right["tile22"]["maxtemp"] = 10
    tiles_right["tile22"]["mintemp"] = 0

    # Tile 23
    temp_data = []
    for i in range(0,len(tiles_right["tile23"]["coordinatesX"])):
        x = tiles_right["tile23"]["coordinatesX"][i]
        y = tiles_right["tile23"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile23"]["tempdata"] = temp_data
    tiles_right["tile23"]["meantemp"] = mean(temp_data)
    tiles_right["tile23"]["maxtemp"] = 10
    tiles_right["tile23"]["mintemp"] = 0

    # Tile 24
    temp_data = []
    for i in range(0,len(tiles_right["tile24"]["coordinatesX"])):
        x = tiles_right["tile24"]["coordinatesX"][i]
        y = tiles_right["tile24"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile24"]["tempdata"] = temp_data
    tiles_right["tile24"]["meantemp"] = mean(temp_data)
    tiles_right["tile24"]["maxtemp"] = 10
    tiles_right["tile24"]["mintemp"] = 0

    # Tile 25
    temp_data = []
    for i in range(0,len(tiles_left["tile25"]["coordinatesX"])):
        x = tiles_left["tile25"]["coordinatesX"][i]
        y = tiles_left["tile25"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile25"]["tempdata"] = temp_data
    tiles_left["tile25"]["meantemp"] = mean(temp_data)
    tiles_left["tile25"]["maxtemp"] = 10
    tiles_left["tile25"]["mintemp"] = 0

    # Tile 26
    temp_data = []
    for i in range(0,len(tiles_left["tile26"]["coordinatesX"])):
        x = tiles_left["tile26"]["coordinatesX"][i]
        y = tiles_left["tile26"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile26"]["tempdata"] = temp_data
    tiles_left["tile26"]["meantemp"] = mean(temp_data)
    tiles_left["tile26"]["maxtemp"] = 10
    tiles_left["tile26"]["mintemp"] = 0

    # Tile 27
    temp_data = []
    for i in range(0,len(tiles_left["tile27"]["coordinatesX"])):
        x = tiles_left["tile27"]["coordinatesX"][i]
        y = tiles_left["tile27"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile27"]["tempdata"] = temp_data
    tiles_left["tile27"]["meantemp"] = mean(temp_data)
    tiles_left["tile27"]["maxtemp"] = 10
    tiles_left["tile27"]["mintemp"] = 0

    # Tile 28
    temp_data = []
    for i in range(0,len(tiles_right["tile28"]["coordinatesX"])):
        x = tiles_right["tile28"]["coordinatesX"][i]
        y = tiles_right["tile28"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile28"]["tempdata"] = temp_data
    tiles_right["tile28"]["meantemp"] = mean(temp_data)
    tiles_right["tile28"]["maxtemp"] = 10
    tiles_right["tile28"]["mintemp"] = 0

    # Tile 29
    temp_data = []
    for i in range(0,len(tiles_right["tile29"]["coordinatesX"])):
        x = tiles_right["tile29"]["coordinatesX"][i]
        y = tiles_right["tile29"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile29"]["tempdata"] = temp_data
    tiles_right["tile29"]["meantemp"] = mean(temp_data)
    tiles_right["tile29"]["maxtemp"] = 10
    tiles_right["tile29"]["mintemp"] = 0

    # Tile 30
    temp_data = []
    for i in range(0,len(tiles_right["tile30"]["coordinatesX"])):
        x = tiles_right["tile30"]["coordinatesX"][i]
        y = tiles_right["tile30"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile30"]["tempdata"] = temp_data
    tiles_right["tile30"]["meantemp"] = mean(temp_data)
    tiles_right["tile30"]["maxtemp"] = 10
    tiles_right["tile30"]["mintemp"] = 0

    # Tile 32
    temp_data = []
    for i in range(0,len(tiles_left["tile32"]["coordinatesX"])):
        x = tiles_left["tile32"]["coordinatesX"][i]
        y = tiles_left["tile32"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile32"]["tempdata"] = temp_data
    tiles_left["tile32"]["meantemp"] = mean(temp_data)
    tiles_left["tile32"]["maxtemp"] = 10
    tiles_left["tile32"]["mintemp"] = 0

    # Tile 33
    temp_data = []
    for i in range(0,len(tiles_left["tile33"]["coordinatesX"])):
        x = tiles_left["tile33"]["coordinatesX"][i]
        y = tiles_left["tile33"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile33"]["tempdata"] = temp_data
    tiles_left["tile33"]["meantemp"] = mean(temp_data)
    tiles_left["tile33"]["maxtemp"] = 10
    tiles_left["tile33"]["mintemp"] = 0

    # Tile 34
    temp_data = []
    for i in range(0,len(tiles_right["tile34"]["coordinatesX"])):
        x = tiles_right["tile34"]["coordinatesX"][i]
        y = tiles_right["tile34"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile34"]["tempdata"] = temp_data
    tiles_right["tile34"]["meantemp"] = mean(temp_data)
    tiles_right["tile34"]["maxtemp"] = 10
    tiles_right["tile34"]["mintemp"] = 0

    # Tile 35
    temp_data = []
    for i in range(0,len(tiles_right["tile35"]["coordinatesX"])):
        x = tiles_right["tile35"]["coordinatesX"][i]
        y = tiles_right["tile35"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile35"]["tempdata"] = temp_data
    tiles_right["tile35"]["meantemp"] = mean(temp_data)
    tiles_right["tile35"]["maxtemp"] = 10
    tiles_right["tile35"]["mintemp"] = 0

    ## Define Trays
    # Define Tray 1
    tray1 = {}
    tray1["tile2"] = tiles_left["tile2"]
    tray1["tile3"] = tiles_left["tile3"]
    tray1["tile4"] = tiles_right["tile4"]
    tray1["tile5"] = tiles_right["tile5"]
    #print("Tray 1, Tile 2:"+str(tray1["tile2"]["meantemp"])+" C")
    #print("Tray 1, Tile 3:"+str(tray1["tile3"]["meantemp"])+" C")
    #print("Tray 1, Tile 4:"+str(tray1["tile4"]["meantemp"])+" C")
    #print("Tray 1, Tile 5:"+str(tray1["tile5"]["meantemp"])+" C")
    #print()
    # Define Tray 2
    tray2 = {}
    tray2["tile7"] = tiles_left["tile7"]
    tray2["tile8"] = tiles_left["tile8"]
    tray2["tile9"] = tiles_left["tile9"]
    tray2["tile10"] = tiles_right["tile10"]
    tray2["tile11"] = tiles_right["tile11"]
    tray2["tile12"] = tiles_right["tile12"]
    #print("Tray 2, Tile 7:"+str(tray2["tile7"]["meantemp"])+" C")
    #print("Tray 2, Tile 8:"+str(tray2["tile8"]["meantemp"])+" C")
    #print("Tray 2, Tile 9:"+str(tray2["tile9"]["meantemp"])+" C")
    #print("Tray 2, Tile 10:"+str(tray2["tile10"]["meantemp"])+" C")
    #print("Tray 2, Tile 11:"+str(tray2["tile11"]["meantemp"])+" C")
    #print("Tray 2, Tile 12:"+str(tray2["tile12"]["meantemp"])+" C")
    #print()
    # Define Tray 3
    tray3 = {}
    tray3["tile13"] = tiles_left["tile13"]
    tray3["tile14"] = tiles_left["tile14"]
    tray3["tile15"] = tiles_left["tile15"]
    tray3["tile16"] = tiles_right["tile16"]
    tray3["tile17"] = tiles_right["tile17"]
    tray3["tile18"] = tiles_right["tile18"]
    #print("Tray 3, Tile 13:"+str(tray3["tile13"]["meantemp"])+" C")
    #print("Tray 3, Tile 14:"+str(tray3["tile14"]["meantemp"])+" C")
    #print("Tray 3, Tile 15:"+str(tray3["tile15"]["meantemp"])+" C")
    #print("Tray 3, Tile 16:"+str(tray3["tile16"]["meantemp"])+" C")
    #print("Tray 3, Tile 17:"+str(tray3["tile17"]["meantemp"])+" C")
    #print("Tray 3, Tile 18:"+str(tray3["tile18"]["meantemp"])+" C")
    #print()
    # Define Tray 4
    tray4 = {}
    tray4["tile19"] = tiles_left["tile19"]
    tray4["tile20"] = tiles_left["tile20"]
    tray4["tile21"] = tiles_left["tile21"]
    tray4["tile22"] = tiles_right["tile22"]
    tray4["tile23"] = tiles_right["tile23"]
    tray4["tile24"] = tiles_right["tile24"]
    #print("Tray 4, Tile 19:"+str(tray4["tile19"]["meantemp"])+" C")
    #print("Tray 4, Tile 20:"+str(tray4["tile20"]["meantemp"])+" C")
    #print("Tray 4, Tile 21:"+str(tray4["tile21"]["meantemp"])+" C")
    #print("Tray 4, Tile 22:"+str(tray4["tile22"]["meantemp"])+" C")
    #print("Tray 4, Tile 23:"+str(tray4["tile23"]["meantemp"])+" C")
    #print("Tray 4, Tile 24:"+str(tray4["tile24"]["meantemp"])+" C")
    #print()
    # Define Tray 5
    tray5 = {}
    tray5["tile25"] = tiles_left["tile25"]
    tray5["tile26"] = tiles_left["tile26"]
    tray5["tile27"] = tiles_left["tile27"]
    tray5["tile28"] = tiles_right["tile28"]
    tray5["tile29"] = tiles_right["tile29"]
    tray5["tile30"] = tiles_right["tile30"]
    #print("Tray 5, Tile 25:"+str(tray5["tile25"]["meantemp"])+" C")
    #print("Tray 5, Tile 26:"+str(tray5["tile26"]["meantemp"])+" C")
    #print("Tray 5, Tile 27:"+str(tray5["tile27"]["meantemp"])+" C")
    #print("Tray 5, Tile 28:"+str(tray5["tile28"]["meantemp"])+" C")
    #print("Tray 5, Tile 29:"+str(tray5["tile29"]["meantemp"])+" C")
    #print("Tray 5, Tile 30:"+str(tray5["tile30"]["meantemp"])+" C")
    #print()
    # Define Tray 6
    tray6 = {}
    tray6["tile32"] = tiles_left["tile32"]
    tray6["tile33"] = tiles_left["tile33"]
    tray6["tile34"] = tiles_right["tile34"]
    tray6["tile35"] = tiles_right["tile35"]
    #print("Tray 6, Tile 32:"+str(tray6["tile32"]["meantemp"])+" C")
    #print("Tray 6, Tile 33:"+str(tray6["tile33"]["meantemp"])+" C")
    #print("Tray 6, Tile 34:"+str(tray6["tile34"]["meantemp"])+" C")
    #print("Tray 6, Tile 35:"+str(tray6["tile35"]["meantemp"])+" C")

    ## Store Final Tile Data
    final_tile_data = {}
    final_tile_data["tray1"] = tray1
    final_tile_data["tray2"] = tray2
    final_tile_data["tray3"] = tray3
    final_tile_data["tray4"] = tray4
    final_tile_data["tray5"] = tray5
    final_tile_data["tray6"] = tray6

    ## Write to File
    temps = write_to_file(final_tile_data)
    return(temps)

# Function: Load Grid Data from External CSV files for each image
# Input:
# Output:
def load_grid_data(side):
    tiles={}
    left_range = [2,3,7,8,9,13,14,15,19,20,21,25,26,27,32,33]
    right_range = [4,5,10,11,12,16,17,18,22,23,24,28,29,30,34,35]
    if side == "left":
        for i in left_range:
            filename = 'ImageJData/Left/tile'+str(i)+'.csv'
            coordinates = load_tile_data(filename)
            tiles["tile"+str(i)] = {"coordinatesX":coordinates[:][0],"coordinatesY":coordinates[:][1]}
    elif side == "right":
        for i in right_range:
            filename = 'ImageJData/Right/tile'+str(i)+'.csv'
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

def write_to_file(data):
    final = []
    try:
        file = open("Outputs/temperatures_output.txt", 'w')
    except IOError:
        print("File not found or path is incorrect")
    # Tray 1
    temps = "0 "
    for i in range(2,6):
        tile = "tile"+str(i)
        line = round(data["tray1"][tile]["meantemp"],2)
        temps += str(line)+" "
    temps+="0\n"
    file.write(temps)
    final.append(temps)
    # Tray 2
    temps = ""
    for i in range(7,13):
        tile = "tile"+str(i)
        line = round(data["tray2"][tile]["meantemp"],2)
        temps += str(line)+" "
    temps += "\n"
    file.write(temps)
    final.append(temps)
    # Tray 3
    temps = ""
    for i in range(13,19):
        tile = "tile"+str(i)
        line = round(data["tray3"][tile]["meantemp"],2)
        temps += str(line)+" "
    temps += "\n"
    file.write(temps)
    final.append(temps)
    # Tray 4
    temps = ""
    for i in range(19,25):
        tile = "tile"+str(i)
        line = round(data["tray4"][tile]["meantemp"],2)
        temps += str(line)+" "
    temps += "\n"
    file.write(temps)
    final.append(temps)
    # Tray 5
    temps = ""
    for i in range(25,31):
        tile = "tile"+str(i)
        line = round(data["tray5"][tile]["meantemp"],2)
        temps += str(line)+" "
    temps += "\n"
    file.write(temps)
    final.append(temps)
    # Tray 6
    temps = "0 0 0 0 0 0\n"
    final.append(temps)
    file.write(temps)
    file.close()
    return(data)

# Function: Load Temp Data for tiles in each image
# Input:
# Output:
def control(data):
    # Tray 1
    tray1 = []
    tray1.append(0)
    for i in range(2,6):
        tile = "tile"+str(i)
        temp = round(data["tray1"][tile]["meantemp"],2)
        tray1.append(temp)
    tray1.append(0)
    #print(tray1)
    # Tray 2
    tray2 = []
    for i in range(7,13):
        tile = "tile"+str(i)
        temp = round(data["tray2"][tile]["meantemp"],2)
        tray2.append(temp)
    #print(tray2)
    # Tray 3
    tray3 = []
    for i in range(13,19):
        tile = "tile"+str(i)
        temp = round(data["tray3"][tile]["meantemp"],2)
        tray3.append(temp)
    #print(tray3)
    # Tray 4
    tray4 = []
    for i in range(19,25):
        tile = "tile"+str(i)
        temp = round(data["tray4"][tile]["meantemp"],2)
        tray4.append(temp)
    #print(tray4)
    # Tray 5
    tray5 = []
    for i in range(25,31):
        tile = "tile"+str(i)
        temp = round(data["tray5"][tile]["meantemp"],2)
        tray5.append(temp)
    #print(tray5)
    # Tray 6
    tray6 = []
    for i in range(1,7):
        tray6.append(0)
    #print(tray6)

    ## Control Decisions -> Send from IP over Serial to Monitor GUI
    control_tray1 = []
    for i in range(0,len(tray1)):
        line = ""
        if tray1[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray1[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray1[i],2))*100))
        control_tray1.append(line)
    #print(control_tray1)
    control_tray2 = []
    for i in range(0,len(tray2)):
        line = ""
        if tray2[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray2[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray2[i],2))*100))
        control_tray2.append(line)
    #print(control_tray2)
    control_tray3 = []
    for i in range(0,len(tray3)):
        line = ""
        if tray3[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray3[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray3[i],2))*100))
        control_tray3.append(line)
    #print(control_tray3)
    control_tray4 = []
    for i in range(0,len(tray4)):
        line = ""
        if tray4[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray4[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray4[i],2))*100))
        control_tray4.append(line)
    #print(control_tray4)
    control_tray5 = []
    for i in range(0,len(tray5)):
        line = ""
        if tray5[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray5[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray5[i],2))*100))
        control_tray5.append(line)
    #print(control_tray5)
    control_tray6 = []
    for i in range(0,len(tray6)):
        line = ""
        if tray6[i] >= 0:
            line+="0"
            line+=" "+str(int(abs(round(tray6[i],2))*100))
        else:
            line+="1"
            line+=" "+str(int(abs(round(tray6[i],2))*100))
        control_tray6.append(line)
    #print(control_tray6)
    # Input to the Serial function
    serial_input=[]
    serial_input.append(control_tray1)
    serial_input.append(control_tray2)
    serial_input.append(control_tray3)
    serial_input.append(control_tray4)
    serial_input.append(control_tray5)
    serial_input.append(control_tray6)
    return(serial_input)

# Function: Load Temp Data for tiles in each image
# Input:
# Output:
def serial_data(input):
    print("\n")

# Call Main Function
if __name__ == '__main__':
    start = time.time()
    data = main() # Temp. data dictionary output
    serial_input = control(data) # Serial data
    serial_data(serial_input) # Serial data communication
    end = time.time()
    print(end-start)

    # 1 LED 0 or 1 - heater off/on - too cold so turn heater on
    # 1 LED for tray on/off - everything is too hot, turn heater off

#####################-----------Close-----------################################
