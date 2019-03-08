#!/usr/bin/env python3
################################################################################
################################################################################
### Feb 28, Horizontal Stitch - "main.py" ######################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 2/20/19   ####################################################
##  Date Modified: 2/28/19  ####################################################
################################################################################
# Main Purpose:
# Action Item:
# Caution:
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
    # Step 7: Concatenate Images
    right = cv2.imread('Inputs/right.png',cv2.IMREAD_COLOR) # First Image
    left = cv2.imread('Inputs/left.png',cv2.IMREAD_COLOR) # Second Image
    image_final = concatenate_images(left,right) # Call function
    # Step 8: Write Final Image
    #write_image("Outputs/FinalImage",image_final) # Write Full Image

    # Current Software Module >> Geometric Stitch
    # Step 1: Create LocateStack function
    # Step 2: Geometric Stitch
    # Step 3: Link up with extract temp module
    # Step 4: Extract useful data from the image
    # Step 5: Determine if temp data is out of range

    # Left Diagonal
    right[24][28][:] = 0;
    right[24][28][0] = 255;
    right[25][27][:] = 0;
    right[25][27][0] = 255;
    right[26][26][:] = 0;
    right[26][26][0] = 255;
    right[27][25][:] = 0;
    right[27][25][0] = 255;
    right[28][24][:] = 0;
    right[28][24][0] = 255;
    right[29][23][:] = 0;
    right[29][23][0] = 255;
    right[30][22][:] = 0;
    right[30][22][0] = 255;
    right[31][21][:] = 0;
    right[31][21][0] = 255;
    right[32][20][:] = 0;
    right[32][20][0] = 255;
    right[33][19][:] = 0;
    right[33][19][0] = 255;
    right[34][18][:] = 0;
    right[34][18][0] = 255;
    right[35][17][:] = 0;
    right[35][17][0] = 255;
    right[36][16][:] = 0;
    right[36][16][0] = 255;
    right[37][15][:] = 0;
    right[37][15][0] = 255;
    right[38][14][:] = 0;
    right[38][14][0] = 255;
    right[39][13][:] = 0;
    right[39][13][0] = 255;
    right[40][12][:] = 0;
    right[40][12][0] = 255;
    right[41][11][:] = 0;
    right[41][11][0] = 255;
    right[42][10][:] = 0;
    right[42][10][0] = 255;
    right[43][9][:] = 0;
    right[43][9][0] = 255;
    right[44][8][:] = 0;
    right[44][8][0] = 255;
    right[45][7][:] = 0;
    right[45][7][0] = 255;
    right[46][6][:] = 0;
    right[46][6][0] = 255;
    right[47][5][:] = 0;
    right[47][5][0] = 255;
    right[48][4][:] = 0;
    right[48][4][0] = 255;
    right[49][3][:] = 0;
    right[49][3][0] = 255;
    right[50][2][:] = 0;
    right[50][2][0] = 255;
    right[51][1][:] = 0;
    right[51][1][0] = 255;
    right[52][0][:] = 0;
    right[52][0][0] = 255;

    # Far Side
    right[24][29][:] = 0;
    right[24][29][0] = 255;
    right[24][30][:] = 0;
    right[24][30][0] = 255;
    right[24][31][:] = 0;
    right[24][31][0] = 255;
    right[24][32][:] = 0;
    right[24][32][0] = 255;
    right[24][33][:] = 0;
    right[24][33][0] = 255;
    right[24][34][:] = 0;
    right[24][34][0] = 255;
    right[24][35][:] = 0;
    right[24][35][0] = 255;
    right[24][36][:] = 0;
    right[24][36][0] = 255;
    right[24][37][:] = 0;
    right[24][37][0] = 255;
    right[24][38][:] = 0;
    right[24][38][0] = 255;
    right[24][39][:] = 0;
    right[24][39][0] = 255;
    right[24][40][:] = 0;
    right[24][40][0] = 255;
    right[24][41][:] = 0;
    right[24][41][0] = 255;
    right[24][42][:] = 0;
    right[24][42][0] = 255;
    right[24][43][:] = 0;
    right[24][43][0] = 255;
    right[24][44][:] = 0;
    right[24][44][0] = 255;
    right[24][45][:] = 0;
    right[24][45][0] = 255;
    right[24][46][:] = 0;
    right[24][46][0] = 255;
    right[24][47][:] = 0;
    right[24][47][0] = 255;
    right[24][48][:] = 0;
    right[24][48][0] = 255;
    right[24][49][:] = 0;
    right[24][49][0] = 255;
    right[24][50][:] = 0;
    right[24][50][0] = 255;
    right[24][51][:] = 0;
    right[24][51][0] = 255;
    right[24][52][:] = 0;
    right[24][52][0] = 255;
    right[24][53][:] = 0;
    right[24][53][0] = 255;
    right[24][54][:] = 0;
    right[24][54][0] = 255;
    right[24][55][:] = 0;
    right[24][55][0] = 255;
    right[24][56][:] = 0;
    right[24][56][0] = 255;
    right[24][57][:] = 0;
    right[24][57][0] = 255;
    right[24][58][:] = 0;
    right[24][58][0] = 255;
    right[24][59][:] = 0;
    right[24][59][0] = 255;
    right[24][60][:] = 0;
    right[24][60][0] = 255;
    right[24][61][:] = 0;
    right[24][61][0] = 255;
    right[24][62][:] = 0;
    right[24][62][0] = 255;
    right[24][63][:] = 0;
    right[24][63][0] = 255;
    right[24][64][:] = 0;
    right[24][64][0] = 255;
    right[24][65][:] = 0;
    right[24][65][0] = 255;
    right[24][66][:] = 0;
    right[24][66][0] = 255;
    right[24][67][:] = 0;
    right[24][67][0] = 255;
    right[24][68][:] = 0;
    right[24][68][0] = 255;
    right[24][69][:] = 0;
    right[24][69][0] = 255;
    right[24][70][:] = 0;
    right[24][70][0] = 255;
    right[24][71][:] = 0;
    right[24][71][0] = 255;
    right[24][72][:] = 0;
    right[24][72][0] = 255;
    right[24][73][:] = 0;
    right[24][73][0] = 255;
    right[24][74][:] = 0;
    right[24][74][0] = 255;
    right[24][75][:] = 0;
    right[24][75][0] = 255;
    right[24][76][:] = 0;
    right[24][76][0] = 255;
    right[24][77][:] = 0;
    right[24][77][0] = 255;
    right[24][78][:] = 0;
    right[24][78][0] = 255;
    right[24][79][:] = 0;
    right[24][79][0] = 255;
    right[24][80][:] = 0;
    right[24][80][0] = 255;
    right[24][81][:] = 0;
    right[24][81][0] = 255;
    right[24][82][:] = 0;
    right[24][82][0] = 255;
    right[24][83][:] = 0;
    right[24][83][0] = 255;
    right[24][84][:] = 0;
    right[24][84][0] = 255;
    right[24][85][:] = 0;
    right[24][85][0] = 255;
    right[24][86][:] = 0;
    right[24][86][0] = 255;
    right[24][87][:] = 0;
    right[24][87][0] = 255;
    right[24][88][:] = 0;
    right[24][88][0] = 255;
    right[24][89][:] = 0;
    right[24][89][0] = 255;
    right[24][90][:] = 0;
    right[24][90][0] = 255;
    right[24][91][:] = 0;
    right[24][91][0] = 255;
    right[24][92][:] = 0;
    right[24][92][0] = 255;
    right[24][93][:] = 0;
    right[24][93][0] = 255;
    right[24][94][:] = 0;
    right[24][94][0] = 255;
    right[24][95][:] = 0;
    right[24][95][0] = 255;
    right[24][96][:] = 0;
    right[24][96][0] = 255;
    right[24][97][:] = 0;
    right[24][97][0] = 255;
    right[24][98][:] = 0;
    right[24][98][0] = 255;
    right[24][99][:] = 0;
    right[24][99][0] = 255;
    right[24][100][:] = 0;
    right[24][100][0] = 255;
    right[24][101][:] = 0;
    right[24][101][0] = 255;
    right[24][102][:] = 0;
    right[24][102][0] = 255;
    right[24][103][:] = 0;
    right[24][103][0] = 255;
    right[24][104][:] = 0;
    right[24][104][0] = 255;
    right[24][105][:] = 0;
    right[24][105][0] = 255;
    right[24][106][:] = 0;
    right[24][106][0] = 255;
    right[24][107][:] = 0;
    right[24][107][0] = 255;
    right[24][108][:] = 0;
    right[24][108][0] = 255;
    right[24][109][:] = 0;
    right[24][109][0] = 255;
    right[24][110][:] = 0;
    right[24][110][0] = 255;
    right[24][111][:] = 0;
    right[24][111][0] = 255;
    right[24][112][:] = 0;
    right[24][112][0] = 255;
    right[24][113][:] = 0;
    right[24][113][0] = 255;
    right[24][114][:] = 0;
    right[24][114][0] = 255;
    right[24][115][:] = 0;
    right[24][115][0] = 255;
    right[24][116][:] = 0;
    right[24][116][0] = 255;
    right[24][117][:] = 0;
    right[24][117][0] = 255;
    right[24][118][:] = 0;
    right[24][118][0] = 255;
    right[24][119][:] = 0;
    right[24][119][0] = 255;
    right[24][120][:] = 0;
    right[24][120][0] = 255;
    right[24][121][:] = 0;
    right[24][121][0] = 255;
    right[24][122][:] = 0;
    right[24][122][0] = 255;
    right[24][123][:] = 0;
    right[24][123][0] = 255;

    # Right Diagonal
    right[25][124][:] = 0;
    right[25][124][0] = 255;
    right[26][125][:] = 0;
    right[26][125][0] = 255;
    right[27][126][:] = 0;
    right[27][126][0] = 255;
    right[28][127][:] = 0;
    right[28][127][0] = 255;
    right[29][128][:] = 0;
    right[29][128][0] = 255;
    right[30][129][:] = 0;
    right[30][129][0] = 255;
    right[31][130][:] = 0;
    right[31][130][0] = 255;
    right[32][131][:] = 0;
    right[32][131][0] = 255;
    right[33][132][:] = 0;
    right[33][132][0] = 255;
    right[34][133][:] = 0;
    right[34][133][0] = 255;
    right[35][134][:] = 0;
    right[35][134][0] = 255;
    right[35][135][:] = 0;
    right[35][135][0] = 255;
    right[36][136][:] = 0;
    right[36][136][0] = 255;
    right[37][137][:] = 0;
    right[37][137][0] = 255;
    right[38][138][:] = 0;
    right[38][138][0] = 255;
    right[39][139][:] = 0;
    right[39][139][0] = 255;
    right[40][140][:] = 0;
    right[40][140][0] = 255;
    right[41][141][:] = 0;
    right[41][141][0] = 255;
    right[42][142][:] = 0;
    right[42][142][0] = 255;
    right[43][143][:] = 0;
    right[43][143][0] = 255;
    right[44][144][:] = 0;
    right[44][144][0] = 255;
    right[45][145][:] = 0;
    right[45][145][0] = 255;
    right[46][146][:] = 0;
    right[46][146][0] = 255;
    right[47][147][:] = 0;
    right[47][147][0] = 255;
    right[48][148][:] = 0;
    right[48][148][0] = 255;
    right[49][149][:] = 0;
    right[49][149][0] = 255;
    right[50][150][:] = 0;
    right[50][150][0] = 255;
    right[51][151][:] = 0;
    right[51][151][0] = 255;
    right[52][152][:] = 0;
    right[52][152][0] = 255;
    right[53][153][:] = 0;
    right[53][153][0] = 255;
    right[54][154][:] = 0;
    right[54][154][0] = 255;
    right[55][155][:] = 0;
    right[55][155][0] = 255;
    right[56][156][:] = 0;
    right[56][156][0] = 255;
    right[57][157][:] = 0;
    right[57][157][0] = 255;
    right[58][158][:] = 0;
    right[58][158][0] = 255;
    right[59][159][:] = 0;
    right[59][159][0] = 255;

    print(right[24][28])
    write_image("Outputs/FinalImage",right) # Write Full Image

def locate_stack():

    return(cut_data)


def concatenate_images(image_first,image_second):
    stack_image_data = np.hstack((image_first,image_second)) # Horizontally Stack Img Data
    result = np.concatenate((image_first,image_second), axis=1) # Concatenate
    return(result)

def load_image(name):
    img = cv2.imread(name)
    return(img)

def write_image(fileName,data):
    cv2.imwrite(str(fileName)+".png",data)

if __name__ == '__main__':
    main()
#####################-----------Close-----------################################
