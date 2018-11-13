import math
import cv2
import time
import numpy as np
from matplotlib import pyplot as pylepton

# Object Detection
# Contours

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)

def orb_stitch(img1,img2):
    # Initialization of the Feature Detector
    orb = cv2.ORB_create()
    # Locate keypoints in the image
    kp = orb.detect(img1)
    kp2 = orb.detect(img2)
    # Calculate descriptors for the image
    kp, desc = orb.compute(img1,kp)
    kp2, desc2 = orb.compute(img2,kp2)
    # Create BFMatcher object for Matching Images
    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    # Match Descriptor, Similar Features between 2 Images
    matches = bf.match(desc,desc2)
    # Sort the matches in order of distance for sitching/meshing
    matches_final = sorted(matches, key = lambda x:x.distance)
    # Remove "BAD" matches (85% threshold, only keep top 15% of matches)
    goodMatches = int(len(matches_final)*0.15)
    matches_final = matches_final[:goodMatches]
    # Draw the Keypoints in the image
    img3 = cv2.drawMatches(img1,kp,img2,kp2,matches_final[:],None,flags=2)


# Noise Removal
def noise_removal(img1,img2):
    img_new = img1-img2 # Difference
    return(img_new)

def main():
    start = time.time()
    # Image 1
    img = load_image('IR_0560.jpg')
    img_subtract = load_image('IR_0560.jpg')
    img = noise_removal(img,img_subtract)
    # Image 2
    img2 = load_image('IR_0560.jpg')
    img_subtract2 = load_image('IR_0560.jpg')
    img = noise_removal(img2,img_subtract2)
    # Clean up the image
    gray = gray_scale(img)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)
    gray = np.float32(gray)

if __name__ == "__main__":
    runtime = main() # Functionality
    # Remove noise ->
