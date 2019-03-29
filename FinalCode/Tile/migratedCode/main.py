#!/usr/bin/env python3
################################################################################
################################################################################
### ImageSlicing - "main.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/25/19   ####################################################
##  Date Modified: 3/29/19  #####################################################
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
    print(len(temps[0]))
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
    # Row 6
    num41=0; max41=0; min41=temps[100][0];
    num42=0; max42=0; min42=temps[100][20];
    num43=0; max43=0; min43=temps[100][40];
    num44=0; max44=0; min44=temps[100][60];
    num45=0; max45=0; min45=temps[100][80];
    num46=0; max46=0; min46=temps[100][100];
    num47=0; max47=0; min47=temps[100][120];
    num48=0; max48=0; min48=temps[100][140];

    ## Divide Data into 20X20 Squares
    for idx in range(0,len(temps[0])):
        row = []
        for idy in range(0,len(temps)):
            #find_temp_max(a,b,c,d)
            # Case 1: Tile 1 Quadrant
            if (idx < 20 and idy < 20):
                num1+=1;
                #print("Before in K:"+str(temps[idy][idx]))
                temp = temps[idy][idx]/100 - 273.15
                #print("After in C:"+str(temp))
                #print(temp)
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
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
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max8):
                    max8 = temp
                elif (temp < min8):
                    min8 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 9: Tile 9 Quadrant
            elif (idx < 20 and idy >= 20 and idy < 40):
                num9+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max9):
                    max9 = temp
                elif (temp < min9):
                    min9 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 10: Tile 10 Quadrant
            elif (idx >= 20 and idx < 40 and idy >= 20 and idy < 40):
                num10+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max10):
                    max10 = temp
                elif (temp < min10):
                    min10 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 11: Tile 11 Quadrant
            elif (idx >= 40 and idx < 60 and idy >= 20 and idy < 40):
                num11+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max11):
                    max11 = temp
                elif (temp < min11):
                    min11 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 12: Tile 12 Quadrant
            elif (idx >= 60 and idx < 80 and idy >= 20 and idy < 40):
                    num12+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max12):
                        max12 = temp
                    elif (temp < min12):
                        min12 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 13: Tile 13 Quadrant
            elif (idx >= 80 and idx < 100 and idy >= 20 and idy < 40):
                    num13+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max13):
                        max13 = temp
                    elif (temp < min13):
                        min13 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 14: Tile 14 Quadrant
            elif (idx >= 100 and idx < 120 and idy >= 20 and idy < 40):
                    num14+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max14):
                        max14 = temp
                    elif (temp < min14):
                        min14 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 15: Tile 15 Quadrant
            elif (idx >= 120 and idx < 140 and idy >= 20 and idy < 40):
                    num15+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max15):
                        max15 = temp
                    elif (temp < min15):
                        min15 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 16: Tile 16 Quadrant
            elif (idx >= 140 and idx < 160 and idy >= 20 and idy < 40):
                    num16+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max16):
                        max16 = temp
                    elif (temp < min16):
                        min16 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 17: Tile 17 Quadrant
            elif (idx < 20 and idy >= 40 and idy < 60):
                    num17+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max17):
                        max17 = temp
                    elif (temp < min17):
                        min17 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 18: Tile 18 Quadrant
            elif (idx >= 20 and idx < 40 and idy >= 40 and idy < 60):
                    num18+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max18):
                        max18 = temp
                    elif (temp < min18):
                        min18 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 19: Tile 19 Quadrant
            elif (idx >= 40 and idx < 60 and idy >= 40 and idy < 60):
                    num19+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max19):
                        max19 = temp
                    elif (temp < min19):
                        min19 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 20: Tile 20 Quadrant
            elif (idx >= 60 and idx < 80 and idy >= 40 and idy < 60):
                    num20+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max20):
                        max20 = temp
                    elif (temp < min20):
                        min20 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 21: Tile 21 Quadrant
            elif (idx >= 80 and idx < 100 and idy >= 40 and idy < 60):
                    num21+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max21):
                        max21 = temp
                    elif (temp < min21):
                        min21 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 22: Tile 22 Quadrant
            elif (idx >= 100 and idx < 120 and idy >= 40 and idy < 60):
                    num22+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max22):
                        max22 = temp
                    elif (temp < min22):
                        min22 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 23: Tile 23 Quadrant
            elif (idx >= 120 and idx < 140 and idy >= 40 and idy < 60):
                    num23+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max23):
                        max23 = temp
                    elif (temp < min23):
                        min23 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 24: Tile 24 Quadrant
            elif (idx >= 140 and idx < 160 and idy >= 40 and idy < 60):
                    num24+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max24):
                        max24 = temp
                    elif (temp < min24):
                        min24 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 25: Tile 25 Quadrant
            elif (idx < 20 and idy >= 60 and idy < 80):
                    num25+=1
                    temp = temps[idy][idx]/100 - 273.15
                    if (temp > max25):
                        max25 = temp
                    elif (temp < min25):
                        min25 = temp
                    #print("Tile 8 Quadrant")
                    row.append(temps[idy][idx])
                    #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 26: Tile 26 Quadrant
            elif (idx >= 20 and idx < 40 and idy >= 60 and idy < 80):
                num26+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max26):
                    max26 = temp
                elif (temp < min26):
                    min26 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 27: Tile 27 Quadrant
            elif (idx >= 40 and idx < 60 and idy >= 60 and idy < 80):
                num27+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max27):
                    max27 = temp
                elif (temp < min27):
                    min27 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 28: Tile 28 Quadrant
            elif (idx >= 60 and idx < 80 and idy >= 60 and idy < 80):
                num28+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max28):
                    max28 = temp
                elif (temp < min28):
                    min28 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 29: Tile 29 Quadrant
            elif (idx >= 80 and idx < 100 and idy >= 60 and idy < 80):
                num29+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max29):
                    max29 = temp
                elif (temp < min29):
                    min29 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 30: Tile 30 Quadrant
            elif (idx >= 100 and idx < 120 and idy >= 60 and idy < 80):
                num30+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max30):
                    max30 = temp
                elif (temp < min30):
                    min30 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 31: Tile 31 Quadrant
            elif (idx >= 120 and idx < 140 and idy >= 60 and idy < 80):
                num31+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max31):
                    max31 = temp
                elif (temp < min31):
                    min31 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 32: Tile 32 Quadrant
            elif (idx >= 140 and idx < 160 and idy >= 60 and idy < 80):
                num32+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max32):
                    max32 = temp
                elif (temp < min32):
                    min32 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 33: Tile 33 Quadrant
            elif (idx < 20 and idy >= 80 and idy < 100):
                num33+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max33):
                    max33 = temp
                elif (temp < min33):
                    min33 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 34: Tile 34 Quadrant
            elif (idx >= 20 and idx < 40 and idy >= 80 and idy < 100):
                num34+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max34):
                    max34 = temp
                elif (temp < min34):
                    min34 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 35: Tile 35 Quadrant
            elif (idx >= 40 and idx < 60 and idy >= 80 and idy < 100):
                num35+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max35):
                    max35 = temp
                elif (temp < min35):
                    min35 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 36: Tile 36 Quadrant
            elif (idx >= 60 and idx < 80 and idy >= 80 and idy < 100):
                num36+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max36):
                    max36 = temp
                elif (temp < min36):
                    min36 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 37: Tile 37 Quadrant
            elif (idx >= 80 and idx < 100 and idy >= 80 and idy < 100):
                num37+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max37):
                    max37 = temp
                elif (temp < min37):
                    min37 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 38: Tile 38 Quadrant
            elif (idx >= 100 and idx < 120 and idy >= 80 and idy < 100):
                num38+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max38):
                    max38 = temp
                elif (temp < min38):
                    min38 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 39: Tile 39 Quadrant
            elif (idx >= 120 and idx < 140 and idy >= 80 and idy < 100):
                num39+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max39):
                    max39 = temp
                elif (temp < min39):
                    min39 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 40: Tile 40 Quadrant
            elif (idx >= 140 and idx < 160 and idy >= 80 and idy < 100):
                num40+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max40):
                    max40 = temp
                elif (temp < min40):
                    min40 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 41: Tile 41 Quadrant
            elif (idx < 20 and idy >= 100 and idy < 120):
                num41+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max41):
                    max41 = temp
                elif (temp < min41):
                    min41 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 42: Tile 42 Quadrant
            elif (idx >= 20 and idx < 40 and idy >= 100 and idy < 120):
                num42+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max42):
                    max42 = temp
                elif (temp < min42):
                    min42 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 43: Tile 43 Quadrant
            elif (idx >= 40 and idx < 60 and idy >= 100 and idy < 120):
                num43+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max43):
                    max43 = temp
                elif (temp < min43):
                    min43 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 44: Tile 44 Quadrant
            elif (idx >= 60 and idx < 80 and idy >= 100 and idy < 120):
                num44+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max44):
                    max44 = temp
                elif (temp < min44):
                    min44 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 45: Tile 45 Quadrant
            elif (idx >= 80 and idx < 100 and idy >= 100 and idy < 120):
                num45+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max45):
                    max45 = temp
                elif (temp < min37):
                    min45 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 46: Tile 46 Quadrant
            elif (idx >= 100 and idx < 120 and idy >= 100 and idy < 120):
                num46+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max46):
                    max46 = temp
                elif (temp < min46):
                    min46 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 47: Tile 47 Quadrant
            elif (idx >= 120 and idx < 140 and idy >= 100 and idy < 120):
                num47+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max47):
                    max47 = temp
                elif (temp < min47):
                    min47 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))
            # Case 48: Tile 48 Quadrant
            elif (idx >= 140 and idx < 160 and idy >= 100 and idy < 120):
                num48+=1
                temp = temps[idy][idx]/100 - 273.15
                if (temp > max48):
                    max48 = temp
                elif (temp < min48):
                    min48 = temp
                #print("Tile 8 Quadrant")
                row.append(temps[idy][idx])
                #print("Dimension: "+str((idx,idy))+" Temperature: "+str(temps[idx][idy]))



        tiles_data.append(row)

    ## Print Number of Saved Elements in Each Tile
    #print(num1);print(num2);print(num3);print(num4);print(num5);print(num6)

    ## Check Max and Min Values
    result = []; results = [];
    # Row 1
    result.append(temp_range_check("1",min1,max1+50))
    result.append(temp_range_check("2",min2,max2))
    result.append(temp_range_check("3",min3,max3))
    result.append(temp_range_check("4",min4,max4))
    result.append(temp_range_check("5",min5,max5))
    result.append(temp_range_check("6",min6-51,max6))
    result.append(temp_range_check("7",min7,max7))
    result.append(temp_range_check("8",min8,max8))
    results.append(result)
    result = [];
    result.append(temp_range_check("9",min9,max9))
    result.append(temp_range_check("10",min10,max10))
    result.append(temp_range_check("11",min11,max11))
    result.append(temp_range_check("12",min12,max12))
    result.append(temp_range_check("13",min13,max13))
    result.append(temp_range_check("14",min13,max14))
    result.append(temp_range_check("15",min13,max15))
    result.append(temp_range_check("16",min13,max16))
    results.append(result)
    result = [];
    result.append(temp_range_check("17",min17,max17))
    result.append(temp_range_check("18",min18,max18))
    result.append(temp_range_check("19",min19,max19))
    result.append(temp_range_check("20",min20,max20))
    result.append(temp_range_check("21",min21,max21))
    result.append(temp_range_check("22",min22,max22))
    result.append(temp_range_check("23",min23,max23))
    result.append(temp_range_check("24",min24,max24))
    results.append(result)
    result = [];
    result.append(temp_range_check("25",min25,max25))
    result.append(temp_range_check("26",min26,max26))
    result.append(temp_range_check("27",min27,max27))
    result.append(temp_range_check("28",min28,max28))
    result.append(temp_range_check("29",min29,max29))
    result.append(temp_range_check("30",min30,max30))
    result.append(temp_range_check("31",min31,max31))
    result.append(temp_range_check("32",min32,max32))
    results.append(result)
    result = [];

    print(max24)



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
    passCheck = True
    if (max > 50):
        passCheck=False
        print("Tile "+str(tile_number)+" failed. Too hot!")
    elif (min < -20):
        print("Tile "+str(tile_number)+" failed. Too cold!")
        passCheck=False
    return(passCheck)

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

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
