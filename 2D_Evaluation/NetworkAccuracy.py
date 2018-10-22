import numpy as np
import math

#change which files to read from and which cheetah data it is analysing (in the for loop)

cetane = [43, 61, 80, 106, 124, 136, 155]
jules1_2 = [70, 89, 97, 136, 168, 173, 184]
jules2_2 = [45, 53, 80, 89, 112, 167, 196, 236]
phantom = [71, 89, 124, 138, 165]
zorro = [83, 140, 150, 163]

#marker labels
names = ['r_eye', 'l_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2', 'l_shoulder', 'l_front_knee', 'l_front_ankle', 'l_front_paw', 'l_hip', 'l_back_knee', 'l_back_ankle', 'l_back_paw']

xy = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ChosenOnes\Jules2-2\Results.csv", delimiter=",", skiprows=1, usecols=[5, 6])

dlcxy = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ToAnalyse\Jules_21122017_Flick2-2_CAM11DeepCut_resnet50_Cheetah-merge2Sept23shuffle1_200000.csv", delimiter=",", skiprows=3, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])

threshold = 0.8
dist = []
dist_diff_total = 0
dist_diff_count = 0
t=0
dist2 = np.empty([len(jules2_2)+1, 21])
#dist2[0,:] = names

for i in jules2_2:
    print(i)
    dist_diff = []
    #dist = []

    for k in range(21):   #21 points (not including lure)
    
        #flag=1
        markerx = []
        markery = []
        markerx.append(xy[k+(t*22), 0])
        markery.append(xy[k+(t*22), 1])
        
        markerx.append(dlcxy[i, k*3])
        markery.append(dlcxy[i, k*3+1])
        #print(markerx)
        #print(markery)
        # print(dlcxy[i, k*3+2])
        # if (dlcxy[i, k*3+2])<0.5:
        #     print('TRUE')
        #     flag=0
            #pass
            
        if (dlcxy[i, k*3+2]<threshold)|(float(markerx[0])<10.0)|(float(markery[0])<10.0):
            flag=0
            #pass
        
        else:
            flag=1
            
        if flag==1:
            print(markerx)
            print(markery)
            x_dist = markerx[0]-markerx[1]
            y_dist = markery[0]-markery[1]
            dist.append(names[k]) 
            dist2[t+1,k] = math.sqrt((x_dist**2)+(y_dist**2))
            dist.append(str(math.sqrt((x_dist**2)+(y_dist**2))))
            dist_diff_total += math.sqrt((x_dist**2)+(y_dist**2))
            print(math.sqrt((x_dist**2)+(y_dist**2)))
            dist_diff_count +=1
    t+=1


print(dist_diff_total/dist_diff_count) #average distance
np.savetxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\PointAnalysis\Jules2-2_Sept23_thresh0.8_dist_diff.csv", dist2, delimiter = ",", fmt="%1.4f")

