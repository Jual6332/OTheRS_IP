#!/usr/bin/env bash

currentDate=""
newFolder="Image_Capture_Data/AprilTesting1" # Data Storage

## Image Sensing Part 1: Create New Folder for Testing
if test -d "$newFolder"; then
  echo "Directory $newFolder exists."
  
else
  echo "Directory $newFolder not found."
  mkdir -p "$newFolder"
  echo "Folder created."
fi

## Image Sensing Part 2:
# Call raw_capture folder file executables
echo "Starting image and temperature data capture."
echo "Finished image and temperature data capture."

## Image Sensing (while loop)

## Onboard Image Post-Processing:
# Stitch
echo "Starting image stitching software module."
python3 stitch.py
echo "Finished image stitching software module."

# Tile
echo "Starting tile software module."
python3 tile.py
echo "Finished tile software module."

# Control
echo "Starting control software module."
python3 control.py
echo "Finished control software module."

# Seral Data Export
echo "Starting serial data software module."
python3 raspi_serial.py
echo "Finished serial data software module."
