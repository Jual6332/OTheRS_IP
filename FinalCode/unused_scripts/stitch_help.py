#!/usr/bin/env python3
################################################################################
################################################################################
### Image Stitching - "main.py" ################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 3/26/19   ####################################################
##  Date Modified: 3/28/19  ####################################################
################################################################################
# Main Purpose: A GUI for selecting stack face data.
#####################---------Libraries---------################################
import pyautogui
from tkinter import *
import time
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
from random import randrange
##################---------Global Variables---------############################
WIDTH = 160
HEIGHT = 120
data = np.zeros((HEIGHT, WIDTH))
#####################---------Main Code---------################################
# Main Function
def main():
    gui();

def gui():
    tk = Tk()
    tk.title('Mouse Pointer Information')
    canvas = Canvas(tk,width=450,height=200)
    canvas.pack()
    ct = canvas.create_text(200,50,text='0000000',fill='red',font=('Courier',15))
    ct2 = canvas.create_text(200,100,text='0000000',fill='red',font=('Courier',15))
    ct3col = canvas.create_rectangle(230,130,250,150,fill='red')
    #ct4time = canvas.create_text(350,180,text='0000000',fill='grey',font=('Courier',10))

    while 1==1:
        pos = pyautogui.position()
        pixcol = pyautogui.screenshot().getpixel(pos)
        canvas.itemconfig(ct,text="Position: "+str(pos))
        canvas.itemconfig(ct2,text="Value: "+str(pixcol))

        tk.update()

if __name__ == '__main__':
    main()
