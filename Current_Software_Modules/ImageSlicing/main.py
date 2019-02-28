#!/usr/bin/env python3
################################################################################
################################################################################
### ImageSlicing - "main.py" ################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/25/19   ####################################################
##  Date Modified: 2/27/19  ####################################################
################################################################################
# Main Purpose: Break up the image into representative tiles, check temp values
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
from random import randrange
##################---------Global Variables---------############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
#####################---------Main Code---------################################
def main():
    # Load Temp Values
    temps = load_temp_values('StackImages/raw1.txt')

    # Store Temp Values, Sort through array
    tiles_data = []
    num1=0
    num2=0
    num7=0
    num13=0
    num19=0
    for idx in range(0,len(temps[0])):
        row = []
        for idy in range(0,len(temps)):
            #find_temp_max(a,b,c,d)
            # Case 1: Tile 1 Quadrant
            if (idx < 8 and idy < 6):
                num1+=1
                print("Tile 1 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 2: Tile 2 Quadrant
            elif (idx > 8 and idx < 16 and idy < 6):
                num2+=1
                print("Tile 2 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 3: Tile 3 Quadrant
            elif (idx > 8 and idx < 16 and idy > 6 and idy < 12):
                num2+=1
                print("Tile 3 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 4: Tile 4 Quadrant
            elif (idx > 16 and idx < 24 and idy > 6 and idy < 12):
                num2+=1
                print("Tile 4 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 7: Tile 7 Quadrant
            elif (idx >= 8 and idx < 16 and idy >= 6 and idy < 12):
                #print(idx)
                num7+=1
                print("Tile 7 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 13: Tile 13 Quadrant
            elif (idx > 16 and idx < 24 and idy > 12 and idy < 18):
                #print("Tile 1 Quadrant")
                num13+=1
                print("Tile 13 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 19: Tile 19 Quadrant
            elif (idx > 24 and idx < 32 and idy > 18 and idy < 24):
                num19+=1
                print("Tile 19 Quadrant")
                row.append(temps[idx][idy])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            elif (idx > 32 and idx < 40 and idy > 24 and idy < 30):
                row.append(temps[idx][idy])
                #print("Dimension: "+str(idx,idy)+" Temperature: "+str(temps[idx][idy]))
        tiles_data.append(row)
    #print(num1);print(num2);print(num3);print(num4);print(num5);print(num6)

    ## Store these values in a 8X6 simplified tile structure
    tiles_data = []

            #if (idx < 8):
            #    row.append
            #else if (idx > 8 and idx < ):

    #row = []


    # Load Image, Remove Whitespace
    # I tried a few different methods for removing the whitespace which arises from
    # saving the PIL image. This custom trim() function seems to work best. - Justin 2/27/19
    def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return im.crop(bbox)

    # Save Trimmed Image
    im = Image.open("output.png") # Open whitespace image
    im = trim(im) # Call trim() function
    im.show() # Show
    im.save("output.png") # Save image

    # Call Image_Slicer
    num_tiles = 20
    tiles = image_slicer.slice('output.png',num_tiles, save=False)
    image_slicer.save_tiles(tiles,directory='Outputs',prefix='slice',format='png')

    # Overlay Tiles
    for tile in tiles:
        overlay = ImageDraw.Draw(tile.image)
        overlay.text((5,5),str(tile.number),(255,255,255),ImageFont.load_default()) # Draw #s on the image
    image_slicer.save_tiles(tiles,directory='Outputs/NumberedTiles',prefix='slice',format='png') # Each numbered tiles
    image = join(tiles) # Join tiled images
    image.save('watch-join.png') # Save final image

    # Test Temp Values for the Individual Images
    #im_new = cv2.imread("Outputs/slice_01_01.png",cv2.IMREAD_COLOR) # Second Image
    #im_new = Image.open("Outputs/slice_01_01.png") # Open whitespace image
    #print(im_new)

def find_temp_max(a,b,c,d):
    max = a[0]; idx = 0
    the_rest = []
    the_rest.append(b)
    the_rest.append(c)
    the_rest.append(d)
    while idx < 3:
        temp = the_rest[idx][0]
        if temp > max:
            max = temp
        idx = idx + 1
    print("Max is"+str(max))
    # Print Values for Verification
    print(a)
    print(b)
    print(c)
    print(d)

def find_temp_min(a,b,c,d):
    min = a[0]; idx = 0
    the_rest = []
    the_rest.append(b)
    the_rest.append(c)
    the_rest.append(d)
    while idx < 3:
        temp = the_rest[idx][0]
        if temp < min:
            min = temp
        idx = idx + 1
    print("Min is"+str(min))
    # Print Values for Verification
    print(a)
    print(b)
    print(c)
    print(d)

# Load Temp Values and Write to Image
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
    return data

    # Show, Save the result
    fig = plt.figure(frameon=False)
    ax = plt.subplot(111)
    ax = plt.Axes(fig,[0,0,1,1])
    ax.set_axis_off()
    plt.imshow(data)
    plt.axis('off')
    fig.tight_layout()
    fig.savefig("output.png",pad_inches=0,bbox_inches='tight')

def write_image(fileName,data):
    cv2.imwrite(fileName+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
