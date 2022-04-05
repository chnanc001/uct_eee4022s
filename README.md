# Using DeepLabCut for 3D pose estimation in cheetahs 

This repo demonstrates how to use DeepLabCut for 3D estimation in cheetahs. It is forked from [An Chi Chen](https://github.com/chnanc001). This repo is a co-product of the final year (BSc Eng Mechatronics) project conducted by An Chi Chen at the University of Cape Town. Her masters thesis included using [DeepLabCut](https://github.com/AlexEMG/DeepLabCut) for pose estimation in cheetahs, and is included in the following publication: 

[Using DeepLabCut for 3D markerless pose estimation across species and behaviors](https://www.biorxiv.org/content/10.1101/476531v1)

Tanmay Nath*, Alexander Mathis*, An Chi Chen, Amir Patel, Matthias Bethge, Mackenzie W. Mathis

more information: http://www.mousemotorlab.org/deeplabcut

<p align="center">
<img src="https://static1.squarespace.com/static/57f6d51c9f74566f55ecf271/t/5c3fc1c6758d46950ce7eec7/1547682383595/cheetah.png?format=750w" width="50%">
</p>



## Workflow:

**Camera Calibration:**
   
   Intrinsic: Use [OCamCalib toolbox](https://github.com/urbste/ImprovedOcamCalib) to calibrate the fisheye model camera

   Extrinsic:
   Determine checkerboard/wand points and undistort data using parameters found in the previous step.  
   Using [EasyWand](http://biomech.web.unc.edu/wand-calibration-tools/) determine the extrinsic parameters.  Manually optimise for both wand score and reprojection error.

**2D estimator:**
   Using workflow from [DeepLabCut](https://github.com/AlexEMG/DeepLabCut) train network for task.
    Analyse desired videos using trained network. 

**3D estimator:**
    Undistort data from 2D estimator.  Determine 3D coordinates using DLT triangulation.

## Useful files in this repo:

**/2D_Evaluation** -> for evaluation of trained networks
  - /Hand_Annotate -> contains hand annotated labeles from 5 different markers
  - determineVariation.py.py -> used to calculate the average distance between same points for different markers, for determining acceptable error range for estimation network

  - /Ground_Truth_Data -> contains Analysis Data set (as described in paper) with correct hand-annotated marker locations
  - /Network_Data -> contains marker locations estimated by the 5 different networks produced from this study for the Analysis Data set
  - NetworkAccuracy.py -> script for determining the accuracy of each network, saves raw distances and determines the average, variance and standard deviation
    
  - plotPoints.py -> used to visaulise marker labels
    
**/3D_Evaluation** -> generating and evaluating 3D estimator
  - /CheetahData -> contains network estimated points for cheetah sequences used for reconstruction
  - dlt_reconstruct.py -> adapted from DLTdv5 by Tyson Hedrick, used to calculate and save the 3D points from the 2D marker locations using DLT coefficients obtained from camera calibration
  - limblength.py -> used to determine the limb lengths (as described in paper), saves individual lengths, and determines the varinace and standard deviation of the lengths
  - plot3D -> uses 3D points obtained from dlt_reconstuct.py to plot 3D cheetah skeleton
    
  - examples of outputs from dlt_reconstruct.py and limblength.py can be found in \CetaneSept23 and \ZorroSept23
  
  
## Pre-print:

    @article {NathMathis2018,
        author = {Nath*, Tanmay and Mathis*, Alexander and Chen, An Chi and Patel, Amir and Bethge, Matthias and Mathis, Mackenzie W},
        title = {Using DeepLabCut for 3D markerless pose estimation across species and behaviors},
        year = {2018},
        doi = {10.1101/476531},
        publisher = {Cold Spring Harbor Laboratory},
        URL = {https://www.biorxiv.org/content/early/2018/11/24/476531},
        eprint = {https://www.biorxiv.org/content/early/2018/11/24/476531.full.pdf},
        journal = {bioRxiv}
    }


## License (DEEPLABCUT):

This project is licensed under the GNU Lesser General Public License v3.0. Note that the software is provided "as is", without warranty of any kind, express or implied. If you use this code, please [cite us!](https://www.nature.com/articles/s41593-018-0209-y).
 
