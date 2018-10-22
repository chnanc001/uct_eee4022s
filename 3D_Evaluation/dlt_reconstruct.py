#dlt reconstruct adapted by An Chi Chen from DLTdv5 by Tyson Hedrick

import numpy as np
import csv

def dlt_reconstruct(c,camPts):

    #number of frames
    nFrames=len(camPts)
    #number of cameras
    nCams=len(camPts[0])/2

    #setup output variables
    xyz = np.empty((nFrames, 3))
    rmse = np.empty((nFrames, 1))

    #process each frame
    for i in range(nFrames):
  
        #get a list of cameras with non-NaN [u,v]
        cdx_size = 0
        cdx_temp=np.where(np.isnan(camPts[i-1,0:int(nCams*2)-1:2])==False, 1, 0)
        for x in range(len(cdx_temp)):
            if cdx_temp[x-1] == 1:
                cdx_size = cdx_size + 1
        cdx = np.empty((1, cdx_size))
        for y in range(cdx_size):
            cdx[0][y] = y+1
        
        #print(cdx_size)

        #if we have 2+ cameras, begin reconstructing
        if cdx_size>=2:
    
            #initialize least-square solution matrices
            m1=np.empty((cdx_size*2, 3))
            m2=np.empty((cdx_size*2, 1))

            temp1 = 1
            temp2 = 1
            for z in range(cdx_size*2):
                if z%2==0:
                    m1[z,0]=camPts[i-1,(temp1*2)-2]*c[8,(temp1-1)]-c[0,(temp1-1)]
                    m1[z,1]=camPts[i-1,(temp1*2)-2]*c[9,(temp1-1)]-c[1,(temp1-1)]
                    m1[z,2]=camPts[i-1,(temp1*2)-2]*c[10,(temp1-1)]-c[2,(temp1-1)]
                    m2[z,0]=c[3,temp1-1]-camPts[i-1,(temp1*2)-2]
                    temp1 = temp1+1
                else:
                    m1[z,0]=camPts[i-1,(temp2*2)-1]*c[8,temp2-1]-c[4,temp2-1]
                    m1[z,1]=camPts[i-1,(temp2*2)-1]*c[9,temp2-1]-c[5,temp2-1]
                    m1[z,2]=camPts[i-1,(temp2*2)-1]*c[10,temp2-1]-c[6,temp2-1]
                    m2[z,0]=c[7, temp2-1]-camPts[i-1,(temp2*2)-1]
                    temp2 = temp2+1
            
            #print(temp1)
            #print(temp2)  
            #get the least squares solution to the reconstruction
            Q, R = np.linalg.qr(m1) # QR decomposition with qr function 
            y = np.dot(Q.T, m2) # Let y=Q'.B using matrix multiplication 
            x = np.linalg.solve(R, y) # Solve Rx=y
            xyz_pts = x.transpose()
            
            xyz[i,0:3]=xyz_pts
            #print(xyz)
            #compute ideal [u,v] for each camera
            #uv=m1*xyz[i-1,0:2].transpose
    
            #compute the number of degrees of freedom in the reconstruction
            #dof=m2.size-3
    
            #estimate the root mean square reconstruction error
            #rmse[i,1]=(sum((m2-uv)**2)/dof)^0.5
    
    return xyz



#load dlt coefficient
#c = np.loadtxt(r"D:/UCT Mechatronics/Fourth Year/EEE4022S - Thesis/Cheetah Data/17_12_2017/WandptsCAM7_8/ArgusOutput2-dlt-coefficients.csv", delimiter=",")
c = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\ExtrinsicCal\MiniWand_FixedIntrinsics\EasyWandOutput1_2_undistort_fisheye_dltCoefs.csv", delimiter=",")

#get names of labels
#names = ['r_eye', 'l_eye', 'nose', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2', 'tail3', 'l_shoulder', 'l_front_knee', 'l_front_ankle', 'l_front_paw', 'l_hip', 'l_back_knee', 'l_back_ankle', 'l_back_paw', 'lure']

#names = ['r_eye', 'l_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2', 'l_shoulder', 'l_front_knee', 'l_front_ankle', 'l_front_paw', 'l_hip', 'l_back_knee', 'l_back_ankle', 'l_back_paw']

#half
names = ['r_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2']

j=1
l=1
#m=4
#n=6
#o=10
#p=8

for k in range(len(names)):
    
    #get individual coord
    #hand annotated data
    # CAM1=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(j,j+1))
    # CAM2=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(l,l+1))
    # CAM3=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(m,m+1))
    # CAM4=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(n,n+1))
    # CAM5=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(o,o+1))
    # CAM6=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\HandAnnotated\DLTdv5_data_xypts.csv",dtype=float,delimiter=',',skiprows=29,usecols=(p,p+1)) 
    
    
    #read in data from DLC
    CAM1=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\CetaneRun1.1\CAM1_Sept23_half.csv",dtype=float,delimiter=',',skiprows=3,usecols=(j,j+1))
    CAM2=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\CetaneRun1.1\CAM2_Sept23_half.csv",dtype=float,delimiter=',',skiprows=3,usecols=(l,l+1))
    # CAM3=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\CAM3DeepCut_resnet50_Cheetah-merge3Sept26shuffle1_200000.csv",dtype=float,delimiter=',',skiprows=3,usecols=(j,j+1))
    # CAM4=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\CAM4DeepCut_resnet50_Cheetah-merge3Sept26shuffle1_200000.csv",dtype=float,delimiter=',',skiprows=3,usecols=(l,l+1))
    # CAM5=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\CAM6DeepCut_resnet50_Cheetah-merge3Sept26shuffle1_200000.csv",dtype=float,delimiter=',',skiprows=3,usecols=(l,l+1))
    # CAM6=np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\14_12_2017\LilyFlick1\CAM5DeepCut_resnet50_Cheetah-merge3Sept26shuffle1_200000.csv",dtype=float,delimiter=',',skiprows=3,usecols=(l,l+1))
    
    #print(CAM1)
    #print(CAM2)
    
    #combine
    camPts = np.hstack((CAM1, CAM2))
    #print(camPts)
    #np.savetxt('campts.csv', camPts, delimiter = ',', fmt='%1.4f')
    
    xyz = dlt_reconstruct(c, camPts)
    name = (r'D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\ThreeD_v2\Sept23\Cetane_CAM1_2_'+names[k]+'.csv')
    #print(names[k]+'.csv')

    #save xyz coords in csv file
    np.savetxt(name, xyz, delimiter = ',', fmt='%1.4f')

    #next label
    j = j+3
    l = l+3
    #m = m+12
    #n = n+12
    #o =o+12
    #p = p+12