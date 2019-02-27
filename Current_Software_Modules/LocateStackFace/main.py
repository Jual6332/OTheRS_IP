#!/usr/bin/env python3
################################################################################
################################################################################
### LocateStackFace - "main.py" ################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/15/19   ####################################################
##  Date Modified: 2/21/19  ####################################################
################################################################################

# Main Purpose: Locate stack face, aluminum face

#####################---------Libraries---------################################
import numpy as np
import cv2
import math
import time
import sys
from PIL import Image
from matplotlib import pyplot as plt
from random import randrange

#####################---------Main Code---------################################
def main():
    bottomMount = cv2.imread('StackImages/bottomMount.png',cv2.IMREAD_COLOR) # First Image
    topMount = cv2.imread('StackImages/topMount.png',cv2.IMREAD_COLOR) # Second Image
    print(type(topMount))
    print("Result")

    # Manually Locate Pixels
    bottomMount[113][0][:] = 0;
    bottomMount[113][10][:] = 0;
    bottomMount[112][20][:] = 0;
    bottomMount[111][30][:] = 0;
    bottomMount[110][40][:] = 0;
    bottomMount[109][50][:] = 0;
    bottomMount[108][60][:] = 0;
    bottomMount[107][70][:] = 0;
    bottomMount[106][80][:] = 0;
    bottomMount[104][90][:] = 0;
    bottomMount[102][101][:] = 0;
    #bottomMount[101][110][:] = 0;

    # Along the Stack Face Right Edge
    bottomMount[83][117][:] = 0;
    bottomMount[82][125][:] = 0;
    bottomMount[75][115][:] = 0;
    bottomMount[74][122][:] = 0;
    bottomMount[67][113][:] = 0;
    bottomMount[66][120][:] = 0;
    bottomMount[59][111][:] = 0;
    bottomMount[58][117][:] = 0;
    bottomMount[52][109][:] = 0;
    bottomMount[51][115][:] = 0;
    bottomMount[45][107][:] = 0;
    bottomMount[44][112][:] = 0;
    bottomMount[38][105][:] = 0;
    bottomMount[37][109][:] = 0;
    bottomMount[31][103][:] = 0;
    bottomMount[30][107][:] = 0;

    #bottomMount[106][0][:] = 0;
    #bottomMount[106][10][:] = 0;
    #bottomMount[105][20][:] = 0;
    #bottomMount[104][30][:] = 0;
    #bottomMount[103][40][:] = 0;
    #bottomMount[102][50][:] = 0;
    #bottomMount[101][60][:] = 0;
    #bottomMount[100][70][:] = 0;
    #bottomMount[98][80][:] = 0;
    #bottomMount[96][90][:] = 0;
    #bottomMount[94][100][:] = 0;
    #bottomMount[93][110][:] = 0;

    #bottomMount[113][0][0] = 255;
    #bottomMount[113][10][0] = 255;
    #bottomMount[112][20][0] = 255;
    #bottomMount[111][30][0] = 255;
    #bottomMount[110][40][0] = 255;
    #bottomMount[108][60][0] = 255;
    #bottomMount[107][70][0] = 255;
    #bottomMount[106][80][0] = 255;
    #bottomMount[104][90][0] = 255;
    #bottomMount[102][101][0] = 255;
    #bottomMount[101][110][0] = 255;

    # Send Data from Lower-Right Corner
    a = bottomMount[90][127];
    b = bottomMount[91][119];
    c = bottomMount[97][129];
    d = bottomMount[99][120];
    max = find_temp_max(a,b,c,d)
    min = find_temp_min(a,b,c,d)

    # Box Around the Lower-Right Corner
    bottomMount[99][120][:] = 0;
    bottomMount[97][129][:] = 0;
    bottomMount[90][127][:] = 0;
    bottomMount[91][119][:] = 0;

    # Box Around the Lower-Right Corner
    a = bottomMount[90][127][0] = 255;
    b = bottomMount[91][119][0] = 255;
    c = bottomMount[97][129][0] = 255;
    d = bottomMount[99][120][0] = 255;

    # Along the Stack Face Right Edge
    bottomMount[83][117][0] = 255;
    bottomMount[82][125][0] = 255;
    bottomMount[75][115][0] = 255;
    bottomMount[74][122][0] = 255;
    bottomMount[70][115][0] = 255;
    bottomMount[69][122][0] = 255;
    bottomMount[67][113][0] = 255;
    bottomMount[66][120][0] = 255;
    bottomMount[59][111][0] = 255;
    bottomMount[58][117][0] = 255;
    bottomMount[52][109][0] = 255;
    bottomMount[51][115][0] = 255;
    bottomMount[45][107][0] = 255;
    bottomMount[44][112][0] = 255;
    bottomMount[38][105][0] = 255;
    bottomMount[37][109][0] = 255;
    bottomMount[31][103][0] = 255;
    bottomMount[30][107][0] = 255;

    # Along the Stack Inside Corner
    bottomMount[101][111][:] = 0;
    bottomMount[101][111][0] = 255;

    # Along the Stack Face Bottom Edge
    bottomMount[106][0][0] = 255;
    bottomMount[106][10][0] = 255;
    bottomMount[105][20][0] = 255;
    bottomMount[104][30][0] = 255;
    bottomMount[103][40][0] = 255;
    bottomMount[109][50][0] = 255;
    bottomMount[102][50][0] = 255;
    bottomMount[101][60][0] = 255;
    bottomMount[100][70][0] = 255;
    bottomMount[98][80][0] = 255;
    bottomMount[96][90][0] = 255;
    bottomMount[94][100][0] = 255;
    bottomMount[93][110][0] = 255;

    write_image("Outputs/bottomMount",bottomMount) # Write Full Image

def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data)

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

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
