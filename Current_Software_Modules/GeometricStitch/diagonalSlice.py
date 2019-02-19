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


def diagImgSlice(topx,topy,botx,boty): #output: topDiag, botDiag
    # read input image
    image = cv2.imread('Inputs/rgb1.png',cv2.IMREAD_COLOR); #image

    #initialize arrays to hold each side of slice
    topDiag = np.zeros(image.shape[0:2]);
    botDiag = np.zeros(image.shape[0:2]);


   #define diagonal slice using slope. Simplify to find most accurate diagonal path
    slope = Fraction(boty,topx);
    rise  = slope.numerator;
    run   = slope.denominator;

    #check to make sure imgrabing num cols here
    lenCols = topy;

    riseCount = 0;

    #note: x = rows ---  y = cols
    #iterate through rows starting at topx row and ending at botx row
    for i in range(0,botx-topx):

        if riseCount > rise:
            lenCols -= run;
            riseCount = 1;
        else:
            riseCount+=1;

        topDiag[i,0:lenCols] = image[i,0:lenCols,0];
        botDiag[i,lenCols:-1] = image[i,lenCols:-1,0];

    #write output arrays to png files
    cv2.imwrite("Outputs/topDiag.png",topDiag);
    cv2.imwrite("Outputs/botDiag.png",botDiag);


# diagImgSlice(topx,topy,botx,boty)
diagImgSlice(2,160,120,2) #img is 120,160,3
