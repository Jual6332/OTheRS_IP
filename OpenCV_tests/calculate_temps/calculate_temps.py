import numpy as np
import math
import os
import time
import cv2

def calc_func(pixel,planck_r1,planck_r2,planck_b,planck_o,planck_f):
    K = 273.15;
    temp = planck_b / math.log(planck_r1 / (planck_r2 * (pixel + planck_o)) + planck_f) - K
    return(temp)

def load_image(name):
    img = cv2.imread(name)
    return(img)

def main():
    start = time.time()
    img = load_image('thermal2.jpg')
    B = float(os.environ["B"])
    F = float(os.environ["F"])
    O = float(os.environ["O"])
    R1 = float(os.environ["R1"])
    R2 = float(os.environ["R2"])
    temp_func = np.vectorize(lambda x: calc_func(x,R1,R2,B,O,F))
    ans = temp_func(10)
    end = time.time()
    return(end-start)

if __name__ == "__main__":
    running_times=[] # Running times, for 100 sims
    for i in range(0,100):
        runtime = main() # Functionality
        running_times.append(runtime)
    print(runtime)
    # Average of 50 simulations
    print("Avg run-time is: "+str(100*np.mean(running_times,dtype=np.float32))+" ms.")
