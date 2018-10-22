#AChen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#names of labels
names = ['r_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2']

folder = r'D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\ThreeD_v2\Sept23'


front_thigh_dist = []
front_thigh_total = 0
front_calf_dist = []
front_calf_total = 0
front_paw_dist = []
front_paw_total = 0
spine1_dist = []
spine1_total = 0
spine2_dist = []
spine2_total = 0
back_thigh_dist= []
back_thigh_total = 0
back_calf_dist= []
back_calf_total = 0
back_paw_dist= []
back_paw_total = 0
tail1_dist = []
tail1_total = 0
tail2_dist = []
tail2_total = 0

variance = []


for k in range(100, 200):
    xdata=[]
    ydata=[]
    zdata=[]
    
#read in xyz coords for each marker for frame k
    for i in names:
        xyz_pts = pd.read_csv(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\ThreeD_v2\Sept23\Cetane_CAM1_2_"+i+".csv", skiprows=k, nrows = 1, header=None)
        xdata.append(xyz_pts[0][0])
        ydata.append(xyz_pts[1][0])
        zdata.append(xyz_pts[2][0])


    xface = []
    yface = []
    zface = []

    xfrontleg = []
    yfrontleg = []
    zfrontleg = []

    xback = []  
    yback = []
    zback = []

    xbackleg = []
    ybackleg = []
    zbackleg = []

    xface.append(xdata[0])
    xface.append(xdata[1])
    yface.append(ydata[0])
    yface.append(ydata[1])
    zface.append(zdata[0])
    zface.append(zdata[1])
    
    xfrontleg.append(xdata[1])
    xfrontleg.append(xdata[2])
    xfrontleg.append(xdata[3])
    xfrontleg.append(xdata[4])
    yfrontleg.append(ydata[1])
    yfrontleg.append(ydata[2])
    yfrontleg.append(ydata[3])
    yfrontleg.append(ydata[4])
    zfrontleg.append(zdata[1])
    zfrontleg.append(zdata[2])
    zfrontleg.append(zdata[3])
    zfrontleg.append(zdata[4])
    
    xback.append(xdata[1])
    xback.append(xdata[5])
    xback.append(xdata[6])
    xback.append(xdata[10])
    xback.append(xdata[11])
    yback.append(ydata[1])
    yback.append(ydata[5])
    yback.append(ydata[6])
    yback.append(ydata[10])
    yback.append(ydata[11])
    zback.append(zdata[1])
    zback.append(zdata[5])
    zback.append(zdata[6])
    zback.append(zdata[10])
    zback.append(zdata[11])
    
    
    xbackleg.append(xdata[6])
    xbackleg.append(xdata[7])
    xbackleg.append(xdata[8])
    xbackleg.append(xdata[9])
    ybackleg.append(ydata[6])
    ybackleg.append(ydata[7])
    ybackleg.append(ydata[8])
    ybackleg.append(ydata[9])
    zbackleg.append(zdata[6])
    zbackleg.append(zdata[7])
    zbackleg.append(zdata[8])
    zbackleg.append(zdata[9])

    #distance front thigh
    x_dist = xdata[1]-xdata[2]
    y_dist = ydata[1]-ydata[2]
    z_dist = zdata[1]-zdata[2]
    front_thigh_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    front_thigh_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
    #distance front calf
    x_dist = xdata[3]-xdata[2]
    y_dist = ydata[3]-ydata[2]
    z_dist = zdata[3]-zdata[2]
    front_calf_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    front_calf_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
    #distance front paw
    x_dist = xdata[3]-xdata[4]
    y_dist = ydata[3]-ydata[4]
    z_dist = zdata[3]-zdata[4]
    front_paw_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    front_paw_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
        
    #distance spine 1
    x_dist = xdata[1]-xdata[5]
    y_dist = ydata[1]-ydata[5]
    z_dist = zdata[1]-zdata[5]
    spine1_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    spine1_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
         
    #distance spine 2
    x_dist = xdata[5]-xdata[6]
    y_dist = ydata[5]-ydata[6]
    z_dist = zdata[5]-zdata[6]
    spine2_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    spine2_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
        
    #distance back thigh
    x_dist = xdata[6]-xdata[7]
    y_dist = ydata[6]-ydata[7]
    z_dist = zdata[6]-zdata[7]
    back_thigh_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    back_thigh_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
        
    #distance back calf
    x_dist = xdata[7]-xdata[8]
    y_dist = ydata[7]-ydata[8]
    z_dist = zdata[7]-zdata[8]
    back_calf_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    back_calf_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
    #distance back paw
    x_dist = xdata[9]-xdata[8]
    y_dist = ydata[9]-ydata[8]
    z_dist = zdata[9]-zdata[8]
    back_paw_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    back_paw_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
    #distance tail 1
    x_dist = xdata[6]-xdata[10]
    y_dist = ydata[6]-ydata[10]
    z_dist = zdata[6]-zdata[10]
    tail1_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    tail1_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
    #distance tail 2
    x_dist = xdata[10]-xdata[11]
    y_dist = ydata[10]-ydata[11]
    z_dist = zdata[10]-zdata[11]
    tail2_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    tail2_total += math.sqrt(x_dist**2+y_dist**2+z_dist**2)
    
print('done')

#mean calc
front_thigh_mean = front_thigh_total/len(front_thigh_dist)
front_calf_mean = front_calf_total/len(front_thigh_dist)
front_paw_mean = front_paw_total/len(front_thigh_dist)
spine1_mean = spine1_total/len(front_thigh_dist)
spine2_mean = spine2_total/len(front_thigh_dist)
back_thigh_mean = back_thigh_total/len(front_thigh_dist)
back_calf_mean = back_calf_total/len(front_thigh_dist)
back_paw_mean = back_paw_total/len(front_thigh_dist)
tail1_mean = tail1_total/len(front_thigh_dist)
tail2_mean = tail2_total/len(front_thigh_dist)

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = front_thigh_dist[i]-front_thigh_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = front_calf_dist[i]-front_calf_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = front_paw_dist[i]-front_paw_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = spine1_dist[i]-spine1_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = spine2_dist[i]-spine2_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = back_thigh_dist[i]-back_thigh_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = back_calf_dist[i]-back_calf_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = back_paw_dist[i]-back_paw_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = tail1_dist[i]-tail1_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

diff_total = 0
for i in range(len(front_thigh_dist)):
    diff = tail2_dist[i]-tail2_mean
    diff_square = diff*diff
    diff_total += diff_square
variance.append(diff_total/len(front_thigh_dist))

standard_deviation = []

for v in range(len(variance)):
    standard_deviation.append(math.sqrt(variance[v]))

print(variance)
print(standard_deviation)

#save evaluation data
np.savetxt(folder+r"\front_thigh_distance.csv", front_thigh_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\front_calf_distance.csv", front_calf_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\front_paw_distance.csv", front_paw_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\spine1_distance.csv", spine1_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\spine2_distance.csv", spine2_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\back_thigh_distance.csv", back_thigh_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\back_calf_distance.csv", back_calf_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\back_paw_distance.csv", back_paw_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\tail1_distance.csv", tail1_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\tail2_distance.csv", tail2_dist, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\variance.csv", variance, delimiter = ',', fmt='%1.4f')
np.savetxt(folder+r"\standard_deviation.csv", standard_deviation, delimiter = ',', fmt='%1.4f')