# uct_eee4022s
3D Markerless Body Motion Capture for the Cheetah

This repo is a coproduct of the final year (BSc Eng Mechatronics) project conducted by An Chi Chen at the University of Cape Town. 

# Workflow followed for this final year project:

Camera Calibration:
    Intrinsic:
    Use OCamCalib toolbox from here  to calibrate the fisheye model camera

   Extrinsic:
   Determine checkerboard/wand points and undistort data using parameters found in the previous step
   Using EasyWand (link) determine the extrinsic parameters.  Manually optimise for both wand score and reprojection error.

2D estimator:
   Using workflow from DeepLabCut (link) train network for task.
    Analyse desired videos using trained network. 

3D estimator:
    Undistort data from 2D estimator.  Determine 3D coordinates using DLT triangulation.

# Useful files in this repo:

/2D_Evaluation -> for evaluation of trained networks
    - /Hand_Annotate -> contains hand annotated labeles from 5 different markers
    - determineVariation.py.py -> used to calculate the average distance between same points for different markers, for determining acceptable error range for estimation network

    - /Ground_Truth_Data -> contains Analysis Data set (as described in paper) with correct hand-annotated marker locations
    - /Network_Data -> contains marker locations estimated by the 5 different networks produced from this study for the Analysis Data set
    - NetworkAccuracy.py -> script for determining the accuracy of each network, saves raw distances and determines the average, variance and standard deviation
    
    - plotPoints.py -> used to visaulise marker labels
    
/3D_Evaluation -> generating and evaluating 3D estimator
    -
    
