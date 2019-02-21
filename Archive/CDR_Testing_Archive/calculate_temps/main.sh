#!/bin/bash
Flir=$(exiftool -Flir:all "$1")
Type=$(echo "$Flir" | grep "Raw Thermal Image Type" | cut -d: -f2)

# Find Planck constants
export B=$(echo "$Flir" | grep "Planck B" | sed 's/[^0-9.-]*//g')
export F=$(echo "$Flir" | grep "Planck F" | sed 's/[^0-9.-]*//g')
export O=$(echo "$Flir" | grep "Planck O" | sed 's/[^0-9.-]*//g')
export R1=$(echo "$Flir" | grep "Planck R1" | sed 's/[^0-9.-]*//g')
export R2=$(echo "$Flir" | grep "Planck R2" | sed 's/[^0-9.-]*//g')

# Locate Reflected Temp
export Temp_refl=$(echo "$Flir" | grep "Reflected Apparent Temperature" | sed 's/[^0-9.-]*//g')

# Locate Emissivity
export Emissivity=$(echo "$Flir" | grep "Emissivity" | sed 's/[^0-9.-]*//g')

# Raw Median Temp.
export RAWmedian=$(echo "$Flir" | grep "Raw Value Median" | sed 's/[^0-9.-]*//g') 

# Raw Temp Range
export RAWdelta=$(echo "$Flir" | grep "Raw Value Range" | sed 's/[^0-9.-]*//g') 

# Run stack:
#. ./main.sh IR_image.jpg
#python3 calcTemp.py
