import numpy as np
import math

markers = ["anchi", "chad", "charlie", "pareen", "fiona"]

allpts = np.empty([126, 10])

i = 0
for marker in markers:
    xy = np.loadtxt(marker+"Label.csv", delimiter=",", skiprows=1, usecols=[5, 6])
    allpts[0:126, i*2:i*2+2] = xy
    i+=1
    
dist_diff = []
dist_diff_total = 0
for k in range(126):
    #flag=1
    markerx = []
    markery = []
    markerx.append(allpts[k, 0])
    markery.append(allpts[k, 1])
    markerx.append(allpts[k, 2])
    markery.append(allpts[k, 3])
    markerx.append(allpts[k, 4])
    markery.append(allpts[k, 5])
    markerx.append(allpts[k, 6])
    markery.append(allpts[k, 7])
    markerx.append(allpts[k, 8])
    markery.append(allpts[k, 9])
    
    dist = []
    for j in range(len(markerx)):
        if (float(markerx[j])<10.0)|(float(markery[j])<10.0):
            flag=0
            #print('point bypassed')
            break

        
        flag=1
        dist.append(math.sqrt((markerx[j]**2)+(markery[j]**2)))
        
    
    #print(dist)
    
    if flag==0:
        pass
    
    else:
        #print(dist)
        dist_diff.append(abs(dist[0]-dist[1]))
        dist_diff.append(abs(dist[0]-dist[2]))
        dist_diff.append(abs(dist[0]-dist[3]))
        dist_diff.append(abs(dist[0]-dist[4]))
        dist_diff.append(abs(dist[1]-dist[2]))
        dist_diff.append(abs(dist[1]-dist[3]))
        dist_diff.append(abs(dist[1]-dist[4]))
        dist_diff.append(abs(dist[2]-dist[3]))
        dist_diff.append(abs(dist[2]-dist[4]))
        dist_diff.append(abs(dist[3]-dist[4]))

        
        dist_diff_total += abs(dist[0]-dist[1])
        dist_diff_total += abs(dist[0]-dist[2])
        dist_diff_total += abs(dist[0]-dist[3])
        dist_diff_total += abs(dist[0]-dist[4])
        dist_diff_total += abs(dist[1]-dist[2])
        dist_diff_total += abs(dist[1]-dist[3])
        dist_diff_total += abs(dist[1]-dist[4])
        dist_diff_total += abs(dist[2]-dist[3])
        dist_diff_total += abs(dist[2]-dist[4])
        dist_diff_total += abs(dist[3]-dist[4])
        
        
np.savetxt("dist_diff.csv", dist_diff, delimiter = ",", fmt='%1.4f')
print(dist_diff_total/len(dist_diff))  #average distance

temp_total = 0
for p in range(len(dist_diff)):
    temp = dist_diff[p]-(dist_diff_total/len(dist_diff))
    temp_sq = temp*temp
    temp_total += temp_sq
    
print(temp_total/len(dist_diff))  #variance
print(math.sqrt(temp_total/len(dist_diff))) #standard deviation