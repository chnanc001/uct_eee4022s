import matplotlib.pyplot as plt
from skimage import io
import numpy as np

cetane = [43, 61, 80, 106, 124, 136, 155]
jules1_2 = [70, 89, 97, 136, 168, 173, 184]
jules2_2 = [45, 53, 80, 89, 112, 167, 196, 236]
phantom = [71, 89, 124, 138, 165]
zorro = [83, 140, 150, 163]

test = [173]

handmarkvary = [31, 39, 85, 90, 104, 149]

color = plt.cm.get_cmap('cool', 21)

xy = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ChosenOnes\Jules1-2\Results.csv", delimiter=",", skiprows=1, usecols=[5, 6])

dlcxy = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ToAnalyse\Jules_21122017_Flick1-2_CAM1DeepCut_resnet50_Cheetah-merge2Sept23shuffle1_200000.csv", delimiter=",", skiprows=3, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63])        



t=0
   
for i in jules1_2:
    #print(i)
    dist_diff = []
    #dist = []
    markerx = []
    markery = []
    
    dlcx = []
    dlcy = []
    for k in range(21):   #21 points (not including lure)
        if (dlcxy[i, k*3+2]<0.8)|(float(xy[k+(t*22), 0])<0)|(float(xy[k+(t*22), 1])<0):  #(dlcxy[i, k*3+2]<threshold)|
            #flag=0
            pass
        
        else:
            #flag=1
            markerx.append(xy[k+(t*22), 0])
            markery.append(xy[k+(t*22), 1])
        
            dlcx.append(dlcxy[i, k*3])
            dlcy.append(dlcxy[i, k*3+1])
            
            
    scale=0.5            
    #image = io.imread(r'D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ChosenOnes\Jules2-2\img'+str(i)+'.png')
    
    image = io.imread(r'D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\ChosenOnes\Jules1-2\img'+str(i)+'.png')
    plt.axis('off')
    
    if np.ndim(image)==2:
        h, w = np.shape(image)
    else:
        h, w, nc = np.shape(image)
                
    plt.figure(frameon=False, figsize=(w * 1. / 100 * scale, h * 1. / 100 * scale))
    #plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    
    plt.imshow(image, 'bone')     
    
    for m in range(len(markerx)):
        plt.scatter(x=markerx[m],y=markery[m],color='w', alpha=1,s=10)   #color=color(m), alpha=1,s=10
        plt.text(markerx[m],markery[m],  '%s' % (str(m)), size=10, zorder=1, color='w') 
        plt.scatter(x=dlcx,y=dlcy,color='r',s=6)
        plt.text(dlcx[m],dlcy[m],  '%s' % (str(m)), size=10, zorder=1, color='r')
    
    plt.xlim(0, w)
    plt.ylim(0, h)
    plt.axis('off')
    #plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.gca().invert_yaxis()
    plt.show()
    #plt.savefig(r'data-AnalysisNetwork\Visualisation\Zorro\Zorro_Sept26_img'+str(i)+'.png')
    t+=1
