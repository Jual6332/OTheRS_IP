#!/usr/bin/env bash
################################################################################
################################################################################
### Locate tiles - "main.sh" #################################################
################################################################################
##  Justin A, Pierre G.     ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 4/3/19    ####################################################
##  Date Modified: 4/11/19   ####################################################
################################################################################
# Main Purpose: Send control decisions
#####################---------Libraries---------################################

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
