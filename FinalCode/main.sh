#!/usr/bin/env bash
#which bash
#who = "OTheRS!";
#echo Hello, "$who!"

currentDate=""
newFolder="Image_Capture_Data/MarchTesting"

## Image Sensing Part 1: Create New Folder for Testing
if test -d "$newFolder"; then
  echo "Directory $newFolder exists."
else
  echo "Directory $newFolder not found."
fi

## Image Sensing Part 2:
# Call raw_capture folder file executables

## Image Sensing (while loop)

## Onboard Image Post-Processing:
# Stitch
python3 stitch.py

# Tile
python3 tile.py

# Control

# Seral Data Export
