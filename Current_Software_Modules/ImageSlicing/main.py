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
    # Row 1
    num1=0; max1=0; min1=temps[0][0];
    num2=0; max2=0; min2=temps[0][20];
    num3=0; max3=0; min3=temps[0][40];
    num4=0; max4=0; min4=temps[0][60];
    num5=0; max5=0; min5=temps[0][80];
    num6=0; max6=0; min6=temps[0][100];
    num7=0; max7=0; min7=temps[0][120];
    num8=0; max8=0; min8=temps[0][140];
    # Row 2
    num9=0; max9=0; min9=temps[20][0];
    num10=0; max10=0; min10=temps[20][20];
    num11=0; max11=0; min11=temps[20][40];
    num12=0; max12=0; min12=temps[20][60];
    num13=0; max13=0; min13=temps[20][80];
    num14=0; max14=0; min14=temps[20][100];
    num15=0; max15=0; min15=temps[20][120];
    num16=0; max16=0; min16=temps[20][140];
    # Row 3
    num17=0; max17=0; min17=temps[40][0];
    num18=0; max18=0; min18=temps[40][20];
    num19=0; max19=0; min19=temps[40][40];
    num20=0; max20=0; min20=temps[40][60];
    num21=0; max21=0; min21=temps[40][80];
    num22=0; max22=0; min22=temps[40][100];
    num23=0; max23=0; min23=temps[40][120];
    num24=0; max24=0; min24=temps[40][140];
    # Row 4
    num25=0; max25=0; min25=temps[60][0];
    num26=0; max26=0; min26=temps[60][20];
    num27=0; max27=0; min27=temps[60][40];
    num28=0; max28=0; min28=temps[60][60];
    num29=0; max29=0; min29=temps[60][80];
    num30=0; max30=0; min30=temps[60][100];
    num31=0; max31=0; min31=temps[60][120];
    num32=0; max32=0; min32=temps[60][140];
    # Row 5
    num33=0; max33=0; min33=temps[80][0];
    num34=0; max34=0; min34=temps[80][20];
    num35=0; max35=0; min35=temps[80][40];
    num36=0; max36=0; min36=temps[80][60];
    num37=0; max37=0; min37=temps[80][80];
    num38=0; max38=0; min38=temps[80][100];
    num39=0; max39=0; min39=temps[80][120];
    num40=0; max40=0; min40=temps[80][140];

    ## Divide Data into 20X20 Squares
    for idx in range(0,len(temps[0])):
        row = []
        for idy in range(0,len(temps)):
            #find_temp_max(a,b,c,d)
            # Case 1: Tile 1 Quadrant
            if (idx < 20 and idy < 20):
                num1+=1;
                temp = temps[idy][idx]/1000
                if (temp > max1):
                    max1 = temp
                elif (temp < min1):
                    min1 = temp
                #print("Tile 1 Quadrant")
                row.append(temp)
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 2: Tile 2 Quadrant
            elif (idx >= 20 and idx < 40 and idy < 20):
                num2+=1;
                temp = temps[idy][idx]/1000
                if (temp > max2):
                    max2 = temp
                elif (temp < min2):
                    min2 = temp
                #print("Tile 2 Quadrant")
                row.append(temp)
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 3: Tile 3 Quadrant
            elif (idx >= 40 and idx < 60 and idy < 20):
                num3+=1
                temp = temps[idy][idx]/1000
                if (temp > max3):
                    max3 = temp
                elif (temp < min3):
                    min3 = temp
                #print("Tile 3 Quadrant")
                row.append(temp)
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 4: Tile 4 Quadrant
            elif (idx >= 60 and idx < 80 and idy < 20):
                num4+=1
                temp = temps[idy][idx]/1000
                if (temp > max4):
                    max4 = temp
                elif (temp < min4):
                    min4 = temp
                #print("Tile 4 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 5: Tile 5 Quadrant
            elif (idx >= 80 and idx < 100 and idy < 20):
                num5+=1
                temp = temps[idy][idx]/1000
                if (temp > max5):
                    max5 = temp
                elif (temp < min5):
                    min5 = temp
                #print("Tile 5 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 6: Tile 6 Quadrant
            elif (idx >= 100 and idx < 120 and idy < 20):
                num6+=1
                temp = temps[idy][idx]/1000
                if (temp > max6):
                    max6 = temp
                elif (temp < min6):
                    min6 = temp
                #print("Tile 6 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 7: Tile 7 Quadrant
            elif (idx >= 120 and idx < 140 and idy < 20):
                num7+=1
                temp = temps[idy][idx]/1000
                if (temp > max7):
                    max7 = temp
                elif (temp < min7):
                    min7 = temp
                #print("Tile 7 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 8: Tile 8 Quadrant
            elif (idx >= 140 and idx < 160 and idy < 20):
                num8+=1
                temp = temps[idy][idx]/1000
                if (temp > max8):
                    max8 = temp
                elif (temp < min8):
                    min8 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
        tiles_data.append(row)

    ## Print Number of Saved Elements in Each Tile
    #print(num1);print(num2);print(num3);print(num4);print(num5);print(num6)

    ## Check Max and Min Values
    temp_range_check("1",min1,max1+50)
    temp_range_check("2",min2,max2)
    temp_range_check("3",min3,max3)
    temp_range_check("4",min4,max4)
    temp_range_check("5",min5,max5)
    temp_range_check("6",min6-51,max6)
    temp_range_check("7",min7,max7)
    temp_range_check("8",min8,max8)

    ## Load Image, Remove Whitespace
    # I tried a few different methods for removing the whitespace which arises from
    # saving the PIL image. This custom trim() function seems to work best. - Justin 2/27/19
    def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0))) # New Image
        diff = ImageChops.difference(im, bg) # Diff w background
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return im.crop(bbox) # Return Trimmed Image object

    ## Save Trimmed Image
    im = Image.open("output.png") # Open whitespace image
    im = trim(im) # Call trim() function
    im.show() # Show
    im.save("output.png") # Save image

    ## Call Image_Slicer
    num_tiles = 48
    tiles = image_slicer.slice('output.png',num_tiles, save=False) # Slice into tiles
    image_slicer.save_tiles(tiles,directory='Outputs',prefix='slice',format='png') # Save tiles

    ## Overlay Tiles in Single Joined Image
    for tile in tiles:
        overlay = ImageDraw.Draw(tile.image)
        overlay.text((5,5),str(tile.number),(255,255,255),ImageFont.load_default()) # Draw #s on the image
    image_slicer.save_tiles(tiles,directory='Outputs/NumberedTiles',prefix='slice',format='png') # Each numbered tiles
    image = join(tiles) # Join tiled images
    image.save('watch-join.png') # Save final image

## Check if Temp of Current Tile is Out of Range (Too Hot/Too Low)
def temp_range_check(tile_number,min,max):
    # Outside Range of -20C to 50C
    if (max > 50):
        print("Tile "+str(tile_number)+" failed. Too hot!")
    elif (min < -20):
        print("Tile "+str(tile_number)+" failed. Too cold!")

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
    ax = plt.Axes(fig,[0,0,1,1])
    ax.set_axis_off()
    plt.imshow(data)
    plt.axis('off')
    fig.tight_layout()
    fig.savefig("output.png",pad_inches=0,bbox_inches='tight')
    return data

def write_image(fileName,data):
    cv2.imwrite(fileName+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
