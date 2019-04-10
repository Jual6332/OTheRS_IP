#!/usr/bin/env bash

currentDate=""
newFolder="Image_Capture_Data/MarchTesting" # Data Storage

## Image Sensing Part 1: Create New Folder for Testing
if test -d "$newFolder"; then
  echo "Directory $newFolder exists."
else
  echo "Directory $newFolder not found."
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

# Seral Data Export
