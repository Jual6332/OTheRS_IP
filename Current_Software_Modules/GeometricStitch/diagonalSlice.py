#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
import sys
import pdb
from fractions import Fraction
from matplotlib import pyplot as plt
from random import randrange

def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data);

def diagImgSlice(toprow,topcol,botrow,botcol): #output: topDiag, botDiag
    # read input image
    image = cv2.imread('Inputs/rgb1.png',cv2.IMREAD_COLOR); #image

    #initialize arrays to hold each side of slice
    topDiag = np.zeros(image.shape);
    botDiag = np.zeros(image.shape);

   #define diagonal slice using slope. Simplify to find most accurate diagonal path
    slope = Fraction(botrow-toprow,topcol-botcol);
    rise  = slope.numerator;
    run   = slope.denominator;
    print(rise,run,sep="/")
    #check to make sure imgrabing num cols here
    lenCols = topcol;
    riseCount = 0;

    #iterate through rows starting at topx row and ending at botx row
    for i in range(0,botrow-toprow):

        if riseCount > (rise-1):
            lenCols -= run;
            riseCount = 1;
        else:
            riseCount+=1;

        print(lenCols)
        topDiag[i,:lenCols] = image[i,0:lenCols,:];
        botDiag[i,lenCols:] = image[i,lenCols:,:];

    #write output arrays to png files
    cv2.imwrite("Outputs/topDiag.png",topDiag);
    cv2.imwrite("Outputs/botDiag.png",botDiag);

def diagImgStitch(toprow,topcol,botrow,botcol): #output: topDiag, botDiag
    # read input image
    image1 = cv2.imread('Outputs/topDiag.png',cv2.IMREAD_COLOR); #image 1
    image2 = cv2.imread('Outputs/botDiag.png',cv2.IMREAD_COLOR);#image 2

    finalImage = np.zeros(image1.shape);

   #define diagonal slice using slope. Simplify to find most accurate diagonal path
    slope = Fraction(botrow-toprow,topcol-botcol);
    rise  = slope.numerator;
    run   = slope.denominator;
    print(rise,run,sep="/")
    #check to make sure imgrabing num cols here
    lenCols = topcol;
    riseCount = 0;

    #iterate through rows starting at topx row and ending at botx row
    for i in range(0,botrow-toprow):

        if riseCount > (rise-1):
            lenCols -= run;
            riseCount = 1;
        else:
            riseCount+=1;

        print(lenCols)

        #Left = image1[i,:lenCols,:];
        #Right = image2[i,lenCols:,:];

        finalImage[i,:lenCols,:] = image1[i,:lenCols,:];
        finalImage[i,lenCols:,:] = image2[i,lenCols:,:];

    #write output arrays to png files
    cv2.imwrite("Outputs/StitchedImg.png",finalImage);

# diagImgSlice(toprow,topcol,botrow,botcol)
botrow = 0; botcol = 160; toprow = 120; topcol = 0;

diagImgSlice(0,160,120,0) #img is 120,160,3
diagImgStitch(0,160,120,0)
