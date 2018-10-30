import numpy as np
import cv2
from pylepton import Lepton

# Keep commented out until we can test w FLIR Lepton camera

#with Lepton() as l:
#    a,_ = l.capture()

# Sensor Data is Read-in as 12-bit, extend to 16 bits without loosing data
#cv2.normalize(a,a,0,65535, cv2.NORM_MINMAX)

#np.right_shift(a,8,a) # Fit data into 8 bits

#cv2.imwrite("output.png", np.uint8(a))
