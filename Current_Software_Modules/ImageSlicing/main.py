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
import PIL
import time
import sys
from image_slicer import join
from PIL import Image, ImageDraw, ImageFont, ImageChops
from matplotlib import pyplot as plt
from random import randrange
##################---------Global Variables---------#############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
#####################---------Main Code---------################################
def main():
    # Load Temp Values
    load_temp_values('../TemperatureScalingTests/botLoc/raw1.txt')

    # Load Image, Remove Whitespace
    def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return im.crop(bbox)

    # Save Trimmed Image
    im = Image.open("output.png")
    im = trim(im)
    im.show()
    im.save("output.png")

    # Call Image_Slicer
    num_tiles = 20
    tiles = image_slicer.slice('output.png',num_tiles, save=False)
    image_slicer.save_tiles(tiles,directory='Outputs',prefix='slice',format='png')

    # Overlay tiles
    for tile in tiles:
        overlay = ImageDraw.Draw(tile.image)
        overlay.text((5,5),str(tile.number),(255,255,255),ImageFont.load_default())
    image_slicer.save_tiles(tiles,directory='Outputs/NumberedTiles',prefix='slice',format='png')
    image = join(tiles)
    image.save('watch-join.png')

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

    # Show, Save the result
    fig = plt.figure(frameon=False)
    ax = plt.subplot(111)
    ax = plt.Axes(fig,[0,0,1,1])
    ax.set_axis_off()
    plt.imshow(data)
    #plt.savefig("output.png")
    plt.axis('off')
    fig.tight_layout()
    fig.savefig("output.png",pad_inches=0,bbox_inches='tight')
    #plt.show()

def write_image(fileName,data):
    cv2.imwrite(fileName+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
