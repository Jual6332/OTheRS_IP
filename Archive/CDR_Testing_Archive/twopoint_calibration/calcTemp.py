import numpy as np
import math
import os
#import cv2
from PIL import Image
from matplotlib import pyplot as plt

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

#1. Import Exiftool Variables to Python
B = float(os.environ["B"])
F = float(os.environ["F"])
O = float(os.environ["O"])
R1 = float(os.environ["R1"])
R2 = float(os.environ["R2"])
Temp_refl = float(os.environ["Temp_refl"])
Emissivity = float(os.environ["Emissivity"])
RAWmedian = float(os.environ["RAWmedian"])
RAWdelta = float(os.environ["RAWdelta"])

# 2. Temp. Calculations
# Calculate RawMax and RawMin of Image
RAWmax = RAWmedian + RAWdelta/2
RAWmin = RAWmedian - RAWdelta/2

# Calculate Raw Obj Temp (Emissivity<1)
RAWrefl = R1/(R2*(math.exp(B/Temp_refl)-F))-O # Sensor Temp_refl -> Calibrated Raw Temp_refl (K)
# Linear to amount of radiance of the reflected objects
RAWobjmax = (RAWmax-(1-Emissivity)*RAWrefl)/Emissivity # Account for emissivity
RAWobjmin = (RAWmin-(1-Emissivity)*RAWrefl)/Emissivity # Account for emissivity
# Both are linear to amt of radiance of the measured object

# Calculate Raw Temp Range for Ideal (Emissivity=1)
Smax = B/math.log(R1/(R2*(RAWmax+O))+F)
Smin = B/math.log(R1/(R2*(RAWmin+O))+F)
Sdelta = Smax - Smin

#3. Calculate Actual Temp. at each Pixel location
# Load image
im = Image.open("IR_0561.jpg")#.convert('LA') # Convert to greyscale for intensity values
pixels = im.load()

im.save("grey_green.png")

#value = math.log(abs(R1/(R2*pixel+O)+F))
#print("Value is: "+str(value))

'''
for i in range(100,250):
        pixel = pixels[i,i][0]
        Tobj = (B/math.log(abs(R1/(R2*(pixel+O)))+F)-Smin)/Sdelta # Actual calibrated temp of object
        print(Tobj)
        print(pixels[i,i][0])
        pixels[i,i] = (0,255)
'''

#bin_counts, bin_edges, patches = plt.hist(im, 256, normed=1, facecolor='g', alpha=0.75)

histogram = im.histogram()
l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]

# R histogram
plt.figure(0)
for i in range(0, 256):
    plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)

# G histogram
plt.figure(1)
for i in range(0, 256):
    plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)

# B histogram
plt.figure(2)
for i in range(0, 256):
    plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)

plt.show()

#print(pixels)
#pixels[100][100] = (0,255)
#im.save("grey_green.png")


