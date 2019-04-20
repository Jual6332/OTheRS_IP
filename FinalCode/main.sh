#!/usr/bin/env bash
################################################################################
################################################################################
### Locate tiles - "main.sh" #################################################
################################################################################
##  Justin A, Pierre G.     ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 4/3/19    ####################################################
##  Date Modified: 4/14/19   ####################################################
################################################################################
# Main Purpose: Send control decisions
#####################---------Libraries---------################################

while true; do
	currentDate=""
	newFolder="Inputs/March24GridTest/Test8/" # Data Storage

	## Image Sensing Part 1: Create New Folder for Testing
	if test -d "$newFolder"; then
	  echo "Directory $newFolder exists."
	else
	  echo "Directory $newFolder not found."
	  mkdir -p "$newFolder"
	  echo "Folder created."
	fi

	## Begin Image Sensing:
	# If cameras are not connected, there will be an issue here
	cd ~
	cd /home/pi/Lepton-3-Module/software/raw_capture
	./raw_capture 0 1 > ../../../OTheRS_IP/FinalCode/Inputs/March24GridTest/Test9/image2
	./raw_capture 0 1 > ../../../OTheRS_IP/FinalCode/Inputs/March24GridTest/Test9/right.txt
	./raw_capture 1 0 > ../../../OTheRS_IP/FinalCode/Inputs/March24GridTest/Test9/image1
	./raw_capture 1 0 > ../../../OTheRS_IP/FinalCode/Inputs/March24GridTest/Test9/left.txt

	# Change back to OTheRS_IP directory
	cd ~
	cd OTheRS_IP/FinalCode

	## Onboard Image Post-Processing:
	# Stitch
	echo "Starting image stitching software module."
	python3 stitch.py Test8
	echo "Finished image stitching software module."

	# Tile
	echo "Starting tile software module."
	python3 tile.py Test8
	echo "Finished tile software module."

	# Seral Data Export
	echo "Starting serial data software module."
	python3 raspi_serial.py
	echo "Finished serial data software module."
done
