#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "tile.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/26/19   ####################################################
##  Date Modified: 4/26/19   ####################################################
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
    fName_left = "Inputs/March24GridTest/"+str(sys.argv[1])+"/left.txt"
    fName_right = "Inputs/March24GridTest/"+str(sys.argv[1])+"/right.txt"

    data_left = load_temp_values(fName_left)/100 - 273.15
    data_right = load_temp_values(fName_right)/100 - 273.15
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
        
        #temp_data.append(-60)
        #temp_data.append(-60)
        #temp_data.append(-60)
        #temp_data.append(-60)
        #print(type(temp_data))

    tiles_left["tile2"]["tempdata"] = temp_data
    tiles_left["tile2"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile2"]["maxtemp"] = max(temp_data)
    tiles_left["tile2"]["mintemp"] = min(temp_data)
    # Tile 3
    temp_data = []
    for i in range(0,len(tiles_left["tile3"]["coordinatesX"])):
        x = tiles_left["tile3"]["coordinatesX"][i]
        y = tiles_left["tile3"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile3"]["tempdata"] = temp_data
    tiles_left["tile3"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile3"]["maxtemp"] = max(temp_data)
    tiles_left["tile3"]["mintemp"] = min(temp_data)
    # Tile 4
    temp_data = []
    for i in range(0,len(tiles_right["tile4"]["coordinatesX"])):
        x = tiles_right["tile4"]["coordinatesX"][i]
        y = tiles_right["tile4"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile4"]["tempdata"] = temp_data
    tiles_right["tile4"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile4"]["maxtemp"] = max(temp_data)
    tiles_right["tile4"]["mintemp"] = min(temp_data)
    # Tile 5
    temp_data = []
    for i in range(0,len(tiles_right["tile5"]["coordinatesX"])):
        x = tiles_right["tile5"]["coordinatesX"][i]
        y = tiles_right["tile5"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile5"]["tempdata"] = temp_data
    tiles_right["tile5"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile5"]["maxtemp"] = max(temp_data)
    tiles_right["tile5"]["mintemp"] = min(temp_data)
    # Tile 7
    temp_data = []
    for i in range(0,len(tiles_left["tile7"]["coordinatesX"])):
        x = tiles_left["tile7"]["coordinatesX"][i]
        y = tiles_left["tile7"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile7"]["tempdata"] = temp_data
    tiles_left["tile7"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile7"]["maxtemp"] = max(temp_data)
    tiles_left["tile7"]["mintemp"] = min(temp_data)
    # Tile 8
    temp_data = []
    for i in range(0,len(tiles_left["tile8"]["coordinatesX"])):
        x = tiles_left["tile8"]["coordinatesX"][i]
        y = tiles_left["tile8"]["coordinatesY"][i]
        val = data_left[x][y]
        temp_data.append(val)
    tiles_left["tile8"]["tempdata"] = temp_data
    tiles_left["tile8"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile8"]["maxtemp"] = max(temp_data)
    tiles_left["tile8"]["mintemp"] = min(temp_data)
    # Tile 9
    temp_data = []
    for i in range(0,len(tiles_left["tile9"]["coordinatesX"])):
        x = tiles_left["tile9"]["coordinatesX"][i]
        y = tiles_left["tile9"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile9"]["tempdata"] = temp_data
    tiles_left["tile9"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile9"]["maxtemp"] = max(temp_data)
    tiles_left["tile9"]["mintemp"] = min(temp_data)
    # Tile 10
    temp_data = []
    for i in range(0,len(tiles_right["tile10"]["coordinatesX"])):
        x = tiles_right["tile10"]["coordinatesX"][i]
        y = tiles_right["tile10"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile10"]["tempdata"] = temp_data
    tiles_right["tile10"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile10"]["maxtemp"] = max(temp_data)
    tiles_right["tile10"]["mintemp"] = min(temp_data)
    # Tile 11
    temp_data = []
    for i in range(0,len(tiles_right["tile11"]["coordinatesX"])):
        x = tiles_right["tile11"]["coordinatesX"][i]
        y = tiles_right["tile11"]["coordinatesY"][i]
        val = data_right[x][y]
        temp_data.append(val)
    tiles_right["tile11"]["tempdata"] = temp_data
    tiles_right["tile11"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile11"]["maxtemp"] = max(temp_data)
    tiles_right["tile11"]["mintemp"] = min(temp_data)
    # Tile 12
    temp_data = []
    for i in range(0,len(tiles_right["tile12"]["coordinatesX"])):
        x = tiles_right["tile12"]["coordinatesX"][i]
        y = tiles_right["tile12"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile12"]["tempdata"] = temp_data
    tiles_right["tile12"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile12"]["maxtemp"] = max(temp_data)
    tiles_right["tile12"]["mintemp"] = min(temp_data)
    # Tile 13
    temp_data = []
    for i in range(0,len(tiles_left["tile13"]["coordinatesX"])):
        x = tiles_left["tile13"]["coordinatesX"][i]
        y = tiles_left["tile13"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile13"]["tempdata"] = temp_data
    tiles_left["tile13"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile13"]["maxtemp"] = max(temp_data)
    tiles_left["tile13"]["mintemp"] = min(temp_data)
    # Tile 14
    temp_data = []
    for i in range(0,len(tiles_left["tile14"]["coordinatesX"])):
        x = tiles_left["tile14"]["coordinatesX"][i]
        y = tiles_left["tile14"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile14"]["tempdata"] = temp_data
    tiles_left["tile14"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile14"]["maxtemp"] = max(temp_data)
    tiles_left["tile14"]["mintemp"] = min(temp_data)
    # Tile 15
    temp_data = []
    for i in range(0,len(tiles_left["tile15"]["coordinatesX"])):
        x = tiles_left["tile15"]["coordinatesX"][i]
        y = tiles_left["tile15"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile15"]["tempdata"] = temp_data
    tiles_left["tile15"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile15"]["maxtemp"] = max(temp_data)
    tiles_left["tile15"]["mintemp"] = min(temp_data)
    # Tile 16
    temp_data = []
    for i in range(0,len(tiles_right["tile16"]["coordinatesX"])):
        x = tiles_right["tile16"]["coordinatesX"][i]
        y = tiles_right["tile16"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile16"]["tempdata"] = temp_data
    tiles_right["tile16"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile16"]["maxtemp"] = max(temp_data)
    tiles_right["tile16"]["mintemp"] = min(temp_data)
    # Tile 17
    temp_data = []
    for i in range(0,len(tiles_right["tile17"]["coordinatesX"])):
        x = tiles_right["tile17"]["coordinatesX"][i]
        y = tiles_right["tile17"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile17"]["tempdata"] = temp_data
    tiles_right["tile17"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile17"]["maxtemp"] = max(temp_data)
    tiles_right["tile17"]["mintemp"] = min(temp_data)
    # Tile 18
    temp_data = []
    for i in range(0,len(tiles_right["tile18"]["coordinatesX"])):
        x = tiles_right["tile18"]["coordinatesX"][i]
        y = tiles_right["tile18"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile18"]["tempdata"] = temp_data
    tiles_right["tile18"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile18"]["maxtemp"] = max(temp_data)
    tiles_right["tile18"]["mintemp"] = min(temp_data)
    # Tile 19
    temp_data = []
    for i in range(0,len(tiles_left["tile19"]["coordinatesX"])):
        x = tiles_left["tile19"]["coordinatesX"][i]
        y = tiles_left["tile19"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile19"]["tempdata"] = temp_data
    tiles_left["tile19"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile19"]["maxtemp"] = max(temp_data)
    tiles_left["tile19"]["mintemp"] = min(temp_data)
    # Tile 20
    temp_data = []
    for i in range(0,len(tiles_left["tile20"]["coordinatesX"])):
        x = tiles_left["tile20"]["coordinatesX"][i]
        y = tiles_left["tile20"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile20"]["tempdata"] = temp_data
    tiles_left["tile20"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile20"]["maxtemp"] = max(temp_data)
    tiles_left["tile20"]["mintemp"] = min(temp_data)
    # Tile 21
    temp_data = []
    for i in range(0,len(tiles_left["tile21"]["coordinatesX"])):
        x = tiles_left["tile21"]["coordinatesX"][i]
        y = tiles_left["tile21"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile21"]["tempdata"] = temp_data
    tiles_left["tile21"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile21"]["maxtemp"] = max(temp_data)
    tiles_left["tile21"]["mintemp"] = min(temp_data)
    # Tile 22
    temp_data = []
    for i in range(0,len(tiles_right["tile22"]["coordinatesX"])):
        x = tiles_right["tile22"]["coordinatesX"][i]
        y = tiles_right["tile22"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile22"]["tempdata"] = temp_data
    tiles_right["tile22"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile22"]["maxtemp"] = max(temp_data)
    tiles_right["tile22"]["mintemp"] = min(temp_data)
    # Tile 23
    temp_data = []
    for i in range(0,len(tiles_right["tile23"]["coordinatesX"])):
        x = tiles_right["tile23"]["coordinatesX"][i]
        y = tiles_right["tile23"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile23"]["tempdata"] = temp_data
    tiles_right["tile23"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile23"]["maxtemp"] = max(temp_data)
    tiles_right["tile23"]["mintemp"] = min(temp_data)
    # Tile 24
    temp_data = []
    for i in range(0,len(tiles_right["tile24"]["coordinatesX"])):
        x = tiles_right["tile24"]["coordinatesX"][i]
        y = tiles_right["tile24"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile24"]["tempdata"] = temp_data
    tiles_right["tile24"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile24"]["maxtemp"] = max(temp_data)
    tiles_right["tile24"]["mintemp"] = min(temp_data)
    # Tile 25
    temp_data = []
    for i in range(0,len(tiles_left["tile25"]["coordinatesX"])):
        x = tiles_left["tile25"]["coordinatesX"][i]
        y = tiles_left["tile25"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile25"]["tempdata"] = temp_data
    tiles_left["tile25"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile25"]["maxtemp"] = max(temp_data)
    tiles_left["tile25"]["mintemp"] = min(temp_data)
    # Tile 26
    temp_data = []
    for i in range(0,len(tiles_left["tile26"]["coordinatesX"])):
        x = tiles_left["tile26"]["coordinatesX"][i]
        y = tiles_left["tile26"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile26"]["tempdata"] = temp_data
    tiles_left["tile26"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile26"]["maxtemp"] = max(temp_data)
    tiles_left["tile26"]["mintemp"] = min(temp_data)
    # Tile 27
    temp_data = []
    for i in range(0,len(tiles_left["tile27"]["coordinatesX"])):
        x = tiles_left["tile27"]["coordinatesX"][i]
        y = tiles_left["tile27"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile27"]["tempdata"] = temp_data
    tiles_left["tile27"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile27"]["maxtemp"] = max(temp_data)
    tiles_left["tile27"]["mintemp"] = min(temp_data)
    # Tile 28
    temp_data = []
    for i in range(0,len(tiles_right["tile28"]["coordinatesX"])):
        x = tiles_right["tile28"]["coordinatesX"][i]
        y = tiles_right["tile28"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile28"]["tempdata"] = temp_data
    tiles_right["tile28"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile28"]["maxtemp"] = max(temp_data)
    tiles_right["tile28"]["mintemp"] = min(temp_data)
    # Tile 29
    temp_data = []
    for i in range(0,len(tiles_right["tile29"]["coordinatesX"])):
        x = tiles_right["tile29"]["coordinatesX"][i]
        y = tiles_right["tile29"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile29"]["tempdata"] = temp_data
    tiles_right["tile29"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile29"]["maxtemp"] = max(temp_data)
    tiles_right["tile29"]["mintemp"] = min(temp_data)
    # Tile 30
    temp_data = []
    for i in range(0,len(tiles_right["tile30"]["coordinatesX"])):
        x = tiles_right["tile30"]["coordinatesX"][i]
        y = tiles_right["tile30"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
        temp_data
    tiles_right["tile30"]["tempdata"] = temp_data
    tiles_right["tile30"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile30"]["maxtemp"] = max(temp_data)
    tiles_right["tile30"]["mintemp"] = min(temp_data)
    # Tile 32
    temp_data = []
    for i in range(0,len(tiles_left["tile32"]["coordinatesX"])):
        x = tiles_left["tile32"]["coordinatesX"][i]
        y = tiles_left["tile32"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile32"]["tempdata"] = temp_data
    tiles_left["tile32"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile32"]["maxtemp"] = max(temp_data)
    tiles_left["tile32"]["mintemp"] = min(temp_data)
    # Tile 33
    temp_data = []
    for i in range(0,len(tiles_left["tile33"]["coordinatesX"])):
        x = tiles_left["tile33"]["coordinatesX"][i]
        y = tiles_left["tile33"]["coordinatesY"][i]
        val = data_left[y][x]
        temp_data.append(val)
    tiles_left["tile33"]["tempdata"] = temp_data
    tiles_left["tile33"]["meantemp"] = find_avg(temp_data)
    tiles_left["tile33"]["maxtemp"] = max(temp_data)
    tiles_left["tile33"]["mintemp"] = min(temp_data)
    # Tile 34
    temp_data = []
    for i in range(0,len(tiles_right["tile34"]["coordinatesX"])):
        x = tiles_right["tile34"]["coordinatesX"][i]
        y = tiles_right["tile34"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile34"]["tempdata"] = temp_data
    tiles_right["tile34"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile34"]["maxtemp"] = max(temp_data)
    tiles_right["tile34"]["mintemp"] = min(temp_data)
    # Tile 35
    temp_data = []
    for i in range(0,len(tiles_right["tile35"]["coordinatesX"])):
        x = tiles_right["tile35"]["coordinatesX"][i]
        y = tiles_right["tile35"]["coordinatesY"][i]
        val = data_right[y][x]
        temp_data.append(val)
    tiles_right["tile35"]["tempdata"] = temp_data
    tiles_right["tile35"]["meantemp"] = find_avg(temp_data)
    tiles_right["tile35"]["maxtemp"] = max(temp_data)
    tiles_right["tile35"]["mintemp"] = min(temp_data)
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
    
def find_avg(array):
	#print("Data points before:"+str(len(array)))
	for item in array:
		if item < -50:
			array.remove(item)
	#print("Data points after:"+str(len(array)))
	return(mean(array))
			

def write_to_file(data):
    final = []
    with open("Outputs/temperatures_output.txt","w"):
        pass
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
    # Tray 2
    tray2 = []
    for i in range(7,13):
        tile = "tile"+str(i)
        temp = round(data["tray2"][tile]["meantemp"],2)
        tray2.append(temp)
    # Tray 3
    tray3 = []
    for i in range(13,19):
        tile = "tile"+str(i)
        temp = round(data["tray3"][tile]["meantemp"],2)
        tray3.append(temp)
    # Tray 4
    tray4 = []
    for i in range(19,25):
        tile = "tile"+str(i)
        temp = round(data["tray4"][tile]["meantemp"],2)
        tray4.append(temp)
    # Tray 5
    tray5 = []
    for i in range(25,31):
        tile = "tile"+str(i)
        temp = round(data["tray5"][tile]["meantemp"],2)
        tray5.append(temp)
    # Tray 6
    tray6 = []
    for i in range(1,7):
        tray6.append(0)
    trays=[]
    trays.append(tray1)
    trays.append(tray2)
    trays.append(tray3)
    trays.append(tray4)
    trays.append(tray5)
    trays.append(tray6)
    return(trays)

# Call Main Function
if __name__ == '__main__':
    start = time.time()
    data = main() # Temp. data dictionary output
    serial_input = control(data) # Serial data
    end = time.time()
    print("Timing Analysis: "+str(end-start)+" s")

    # 1 LED 0 or 1 - heater off/on - too cold so turn heater on
    # 1 LED for tray on/off - everything is too hot, turn heater off

#####################-----------Close-----------################################
