#AChen

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import pandas as pd
import matplotlib.animation as animation
import math

#3D points are saved as one .csv file for each labeled marker.  first col=x, second col=y, third col=z

#create figure for 3D plot
fig = plt.figure(figsize=(37.5, 5)) #figsize=(70, 5
plt.tight_layout()
ax = plt.axes(projection='3d')

#names of labels
names = ['r_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2']

#names = ['r_eye', 'l_eye', 'r_shoulder', 'r_front_knee', 'r_front_ankle', 'r_front_paw', 'spine', 'r_hip', 'r_back_knee', 'r_back_ankle', 'r_back_paw', 'tail1', 'tail2', 'l_shoulder', 'l_front_knee', 'l_front_ankle', 'l_front_paw', 'l_hip', 'l_back_knee', 'l_back_ankle', 'l_back_paw']

#cmap for plotted points
color = plt.cm.get_cmap('cool', len(names))

def plot3D(k):
    #clear plot
    plt.cla()

    xdata=[]
    ydata=[]
    zdata=[]
    
    frontleg_dist= []
    
    #read in xyz coords for each marker for frame k
    o = 0
    for i in names:
        xyz_pts = pd.read_csv(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\Cheetah Data\12_12_2017\ThreeD_v2\Sept23\Cetane_CAM1_2_"+i+".csv", skiprows=k, nrows = 1, header=None)
        
        

        print(xyz_pts)
        xdata.append(xyz_pts[0][0])
        ydata.append(xyz_pts[1][0])
        zdata.append(xyz_pts[2][0])
    

###
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

#########################################
    
    
    # xface_r = []
    # yface_r = []
    # zface_r = []
    # 
    # xface_l = []
    # yface_l = []
    # zface_l = []

   ##   xfrontleg_r = []
    # yfrontleg_r = []
    # zfrontleg_r = []
    # 
    # xfrontleg_l = []
    # yfrontleg_l = []
    # zfrontleg_l = []
    # 
    # xback = []  
    # yback = []
    # zback = []
    # 
    # xbackleg_r = []
    # ybackleg_r = []
    # zbackleg_r = []
    # 
    # xbackleg_l = []
    # ybackleg_l = []
    # zbackleg_l = []

    # xface_r.append(xdata[0])
    # xface_r.append(xdata[2])
    # yface_r.append(ydata[0])
    # yface_r.append(ydata[2])
    # zface_r.append(zdata[0])
    # zface_r.append(zdata[2])
    # 
    # xface_l.append(xdata[1])
    # xface_l.append(xdata[13])
    # yface_l.append(ydata[1])
    # yface_l.append(ydata[13])
    # zface_l.append(zdata[1])
    # zface_l.append(zdata[13])


  ###     xfrontleg_r.append(xdata[2])
    # xfrontleg_r.append(xdata[3])
    # xfrontleg_r.append(xdata[4])
    # xfrontleg_r.append(xdata[5])
    # yfrontleg_r.append(ydata[2])
    # yfrontleg_r.append(ydata[3])
    # yfrontleg_r.append(ydata[4])
    # yfrontleg_r.append(ydata[5])
    # zfrontleg_r.append(zdata[2])
    # zfrontleg_r.append(zdata[3])
    # zfrontleg_r.append(zdata[4])
    # zfrontleg_r.append(zdata[5])
    # 
    # xfrontleg_l.append(xdata[13])
    # xfrontleg_l.append(xdata[14])
    # xfrontleg_l.append(xdata[15])
    # xfrontleg_l.append(xdata[16])
    # yfrontleg_l.append(ydata[13])
    # yfrontleg_l.append(ydata[14])
    # yfrontleg_l.append(ydata[15])
    # yfrontleg_l.append(ydata[16])
    # zfrontleg_l.append(zdata[13])
    # zfrontleg_l.append(zdata[14])
    # zfrontleg_l.append(zdata[15])
    # zfrontleg_l.append(zdata[16])
    # 
    # xback.append(xdata[2])
    # xback.append(xdata[6])
    # #xback.append(xdata[13])
    # #xback.append(xdata[6])
    # xback.append(xdata[7])
    # xback.append(xdata[11])
    # xback.append(xdata[12])
    # #xback.append(xdata[11])
    # #xback.append(xdata[17])
    # #xback.append(xdata[6])
    # yback.append(ydata[2])
    # yback.append(ydata[6])
    # #yback.append(ydata[13])
    # #yback.append(ydata[6])
    # yback.append(ydata[7])
    # yback.append(ydata[11])
    # yback.append(ydata[12])
    # #yback.append(ydata[11])
    # #yback.append(ydata[17])
    # #yback.append(ydata[6])
    # zback.append(zdata[2])
    # zback.append(zdata[6])
    # #zback.append(zdata[13])
    # #zback.append(zdata[6])
    # zback.append(zdata[7])
    # zback.append(zdata[11])
    # zback.append(zdata[12])
    # #zback.append(zdata[11])
    # #zback.append(zdata[17])
    # #zback.append(zdata[6])
    # 
    # xbackleg_r.append(xdata[7])
    # xbackleg_r.append(xdata[8])
    # xbackleg_r.append(xdata[9])
    # xbackleg_r.append(xdata[10])
    # ybackleg_r.append(ydata[7])
    # ybackleg_r.append(ydata[8])
    # ybackleg_r.append(ydata[9])
    # ybackleg_r.append(ydata[10])
    # zbackleg_r.append(zdata[7])
    # zbackleg_r.append(zdata[8])
    # zbackleg_r.append(zdata[9])
    # zbackleg_r.append(zdata[10])
    # 
    # #xbackleg_l.append(xdata[17])
    # xbackleg_l.append(xdata[18])
    # xbackleg_l.append(xdata[19])
    # xbackleg_l.append(xdata[20])
    # #ybackleg_l.append(ydata[17])
    # ybackleg_l.append(ydata[18])
    # ybackleg_l.append(ydata[19])
    # ybackleg_l.append(ydata[20])
    # #zbackleg_l.append(zdata[17])
    # zbackleg_l.append(zdata[18])
    # zbackleg_l.append(zdata[19])
    # zbackleg_l.append(zdata[20])
 
#half#########################################
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
    
    
    #distance
    # x_dist = xdata[1]-xdata[2]
    # y_dist = ydata[1]-ydata[2]
    # z_dist = zdata[1]-zdata[2]
    # frontleg_dist.append(math.sqrt(x_dist**2+y_dist**2+z_dist**2))
    
    
    #ax.set_xlim3d([-2, 4])
    ax.set_xticklabels([])
    #ax.set_xlabel('X')

    #ax.set_ylim3d([-0.2, 0.6])
    ax.set_yticklabels([])
    #ax.set_ylabel('Y')

    #ax.set_zlim3d([0, 3])
    ax.set_zticklabels([])
    #ax.set_zlabel('Z')
    
    ax.xaxis.grid(False)
    
    #change the view/angle
    ax.view_init(-50, 90)

    ax.w_yaxis.set_pane_color((0.3, 0.3, 0.3, 0.3))
    ax.w_xaxis.set_pane_color((0, 0, 0, 0))
    ax.w_zaxis.set_pane_color((0, 0, 0, 0))
    #ax.grid(None)
    
    #plot each point and it's index according to names list
    for i in range(len(xdata)): 
        ax.scatter(xdata[i],ydata[i],zdata[i],c=color(i)) 
    #    ax.text(xdata[i],ydata[i],zdata[i],  '%s' % (str(i)), size=10, zorder=1, color='k') 
    
    #add the limbs
    ##half
    ax.plot(xfrontleg,yfrontleg,zfrontleg, color='k')
    ax.plot(xback,yback,zback, color='k')
    ax.plot(xbackleg,ybackleg,zbackleg, color='k')
    ax.plot(xface, yface, zface, color = 'k')
    
###############   full 
    # ax.plot(xfrontleg_r,yfrontleg_r,zfrontleg_r, color='k')
    # ax.plot(xback,yback,zback, color='k')
    # ax.plot(xbackleg_r,ybackleg_r,zbackleg_r, color='k')
    #ax.plot(xface_r, yface_r, zface_r, color = 'k')
    #ax.plot(xface_l, yface_l, zface_l, color = 'k')
    #ax.plot(xfrontleg_l,yfrontleg_l,zfrontleg_l, color='k')
    #ax.plot(xbackleg_l,ybackleg_l,zbackleg_l, color='k')
    
    #wait for press before moving on to next frame
    #plt.waitforbuttonpress()

ani = animation.FuncAnimation(fig, plot3D, range(1))    #FOR Cetane Sept23 sequence use 89 to 190 every 15th frame
#ani = animation.FuncAnimation(fig, plot3D, [2])





FFwriter = animation.FFMpegWriter(fps=6)
#ani.save('Cetane_Sept23_3DEstimation.mp4', writer = FFwriter)

plt.show()
print('done')
