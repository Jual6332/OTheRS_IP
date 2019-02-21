import cv2

# Load Image Data
def load_image(name):
    img = cv2.imread(name)
    return(img)

# Grayscale Conversion
def gray_scale(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return(gray)

# Otsu Thresholding
def Otsu_thresholding(blur):
    retval, threshold = cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(threshold)
