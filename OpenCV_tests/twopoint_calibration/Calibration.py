import numpy
import time
import cv2

def load_image(name):
    img = cv2.imread(name)
    return(img)

def main():
    start = time.time()
    Raw_Values = load_image('thermal2.jpg')
    new_img = []
    for i in range(0,Raw_Values.shape[0]):
        row = []
        for j in range(0,Raw_Values.shape[1]):
            row.append(calibration(1))
        new_img.append(row)
    # imwrite()
    end = time.time()
    return(end - start)

def calibration(Raw_Values):
    Raw_Low = 10; Raw_High = 50;
    Reference_Low = 5; Reference_High = 70;
    Reference_Range = Reference_High - Reference_Low
    Raw_Range = Raw_High - Raw_Low
    Corrected_Value = (((Raw_Values - Raw_Low)) * (Reference_Range)) / Raw_Range + Reference_Low

if __name__ == "__main__":
    runtime = main() # Functionality
    print(runtime)
