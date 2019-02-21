#!/usr/bin/env python3
import numpy as np
import cv2
import math
import time
import sys
from PIL import Image
from matplotlib import pyplot as plt
from random import randrange

# Function Descriptions
def transpose(array):
    array = array[:]
    n = len(array)
    for i, row in enumerate(array):
        array[i] = row + [None for _ in range(n-len(row))]
    array = zip(*array)
    for i, row in enumerate(array):
        array[i] = [elem for elem in row if elem is not None]
    return array
