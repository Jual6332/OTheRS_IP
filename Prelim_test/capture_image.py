#!/usr/bin/env python3
import numpy as np
import cv2
import time
import os
from pylepton import Lepton

# Enable SPI on the raspberry pi! After bootup,
# SPI is enabled if /dev/spidev0.0 and /deb/spidev0.1 exist.
with Lepton() as l:
    a,_ = l.capture()

# Initialize Array
h, w, ch = img.shape
emptyImg = np.zeros((h, w)) # Image for manipulation

# Sensor Data is Read-in as 14-bit, extend to 16 bits without losing data
test = cv2.normalize(a,emptyImg,0,65535,cv2.NORM_MINMAX)
cv2.imwrite("output.png", np.uint16(a))

# Save to a particular destination
path = "/home/user/Desktop/Python/OTheRS_IP/Prelim_test"
cv2.imwrite(os.path.join(path,"output_image.jpg"),np.uint16(a))
