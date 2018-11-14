import math
import cv2
import time
import imutils
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as pylepton
import matplotlib.pyplot as pylepton
from sklearn.cluster import k_means

def contours(gray):
    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    cv2.bitwise_not(thresh,thresh)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key=cv2.contourArea)
    [x,y,w,h] = cv2.boundingRect(c)

# Grayscale
def gray_scale(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return(gray)

# Geometric Calibration Functionality
#getPerspectiveTransform
#warpPerspectivd

# K-Means
def kmeans(img,Z,K):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    ret, label, center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return(res2)

# Load Image
def load_image(name):
    img = cv2.imread(name)
    return(img)

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)

# ORB Stitching
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

# Remove Glare
def remove_glare(img):
    # Create CLAHE object
    clahe = cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
    # Apply CLAHE to lightness channel
    cl1 = clahe.apply(img)
    return(cl1)

def main():
    start = time.time()
    # Image 1
    img = load_image('cars.jpg')
    img_subtract = load_image('FLIR_first.jpg')
    #img = noise_removal(img,img_subtract)
    img = gray_scale(img)
    img = remove_glare(img)
    cv2.imwrite('Removing Glare.png',img)

    img = load_image('FLIR_first.jpg')

    # Image 2
    img2 = load_image('FLIR_second.jpg')
    img_subtract2 = load_image('FLIR_second.jpg')
    img2 = noise_removal(img2,img_subtract2)

    # Clean up the image
    gray = gray_scale(img)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)
    gray = np.float32(gray)

    # Test Contours
    img = load_image('bulb.png')
    gray = gray_scale(img)
    contours(gray)

    # K-Means
    img = load_image('FLIR_second.jpg')
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    output = kmeans(img,Z,8)
    cv2.imwrite('res2.png',output)

    # Remove Glare + Add colors based on k-means
    img = load_image('FLIR_second.jpg')
    gray = gray_scale(img)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = ((img_hsv > np.array([0,0,230])).astype(np.float32) + (img_hsv > np.array([0,0,230])).astype(np.float32) * (-0.5)+0.5)
    img_partly_darken = cv2.cvtColor(mask*img_hsv, cv2.COLOR_HSV2BGR)
    plt.imshow(cv2.cvtColor(img_partly_darken,cv2.COLOR_BGR2RGB))
    cv2.imwrite("Partly Darken.png",img_partly_darken)

    # Pick Out Green Pixels:
    green_mask = img[:,:,1] > img[:,:,2]
    green_mask = (green_mask.astype(np.uint8))*255
    green_mask = cv2.cvtColor(green_mask,cv2.COLOR_GRAY2BGR)
    green3_mask = (green_mask >0).astype(np.uint8)*255
    img_green = cv2.bitwise_and(green3_mask,img)

    # Add back in Original Image's Colors:
    ret, thr = cv2.threshold(cv2.cvtColor(img_green,cv2.COLOR_BGR2GRAY),10,255,cv2.THRESH_BINARY)
    blue_mask = (cv2.cvtColor(thr,cv2.COLOR_GRAY2BGR)>0).astype(np.uint8)*255
    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    blue_mask = cv2.morphologyEx(blue_mask,cv2.MORPH_OPEN,kernel_open)
    yellow_mask = 255 - blue_mask

    # Use k-means to get the two main colors -- blue and yellow
    pixels = img
    pixels = pixels.reshape(pixels.shape[0]*pixels.shape[1],3)
    [centroids, labels, inertia] = k_means(pixels,2)
    # Blue Channel
    centroids = np.array(sorted(centroids.astype(np.uint8).tolist(),key=lambda x:x[0]))

if __name__ == "__main__":
    runtime = main() # Functionality
    # Remove noise ->
