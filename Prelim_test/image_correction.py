import math
import cv2
import time

start = time.time()

# Object Detection
# Contours

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)

# Noise Removal
def noise_removal(img1,img2):
    img_new = img1-img2 # Difference
    return(img_new)

def main():
    start = time.time()
    img = load_image('IR_0560.jpg')
    img_subtract = load_image('IR_0560.jpg')
    img = noise_removal(img,img_subtract)
    img2 = load_image('IR_0560.jpg')
    img_subtract2 = load_image('IR_0560.jpg')
    img = noise_removal(img2,img_subtract2)
    gray = gray_scale(img)
    thr = Otsu_thresholding(gray)
    cv2.imwrite('Otsu Thresh.png',thr)
    gray = np.float32(gray)

if __name__ == "__main__":
    runtime = main() # Functionality
