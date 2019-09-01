# OTheRS_IP
Image processing and software repository for OTheRS project.
Created: 10/30/2018
Modified: 4/20/18

## Main Software Tasks:
1. Capture image (FLIR Lepton)
2. Image Correction (OpenCV: noise removal, Ohr's thresholding, adaptive thresh., reducing pixel stretch)
3. Image Stitching and Image transformation(ORB, OpenCV)
4. Geometric calibration (OpenCV)
5. Extract temp. at pixel locations (FLIR calibration technique, 14-bit)
6. 2-point Temp. Calibration (thermocouple data - testing, thermistor data - final design)
7. Output to CSV, temp table

## Preferred Method for Software Changes
- Open a new branch if you are going to make changes or improve functionality
- This will be a good identifier for discrepencies in the code 
- If parts of the code cause failure, be able to find these errors and fix/comment them out 
- When you've reached this point and are ready to merge changes, put in a pull request
- Once branch is merged, the team can debug further

## Making a commit to the Master Branch
- git add -A or git add filename.py // Adds changes (all or a single file)
- git commit -m "" // Commit these changes, leave a message on valuable changes. 
// Think, how is this change improving the software? 
// Is this commit really needed?
- git push origin master // Push to master branch

##  How will software development flow for this project?
- Software development is ongoing on a large project, to mitigate bugs in the overall software system. 
- Before jumping into the code, plan your design thinking on paper
- Software is NOT meant to be designed and then implemented last minute, this will cause un-anticipated issues
- Homework: What is the waterfall method for software development? Why does it not work? Make a note of why Agile works.
