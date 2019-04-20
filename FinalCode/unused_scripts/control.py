#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "control.py" ###################################################
################################################################################
##  Justin Alvey            ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 4/1/19   ####################################################
##  Date Modified: 4/26/19   ####################################################
################################################################################
# Main Purpose: Send control decisions
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
def main():
	filename = "Outputs/temperatures_output.txt"
	data = []
	with open(filename, "r") as f:
		for line in f.read().strip().split("\n"):
			try:
				numbers = [float(i) for i in line.strip().split(" ")]
				#print(numbers)
				data.append(numbers)
			except Exception as e:
				print("Exception: {}".format(e))
	#print(data)
	#data[0][0] = -130.0;
	#data[2][2] = 60.0;
	controls=[]
	for item in data:
		row=[]
		for number in item:
			temp_val = float(number)
			if number < -20.0:
				row.append(1)
			else:
				row.append(0)
			if number > 50.0:
				row.append(2)
		controls.append(row)
	#print(controls)
		
# Call Main Function
if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print("Timing Analysis: "+str(end-start)+" s")
#####################-----------Close-----------################################
