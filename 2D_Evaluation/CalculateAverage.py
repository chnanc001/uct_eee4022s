import numpy as np

cetane = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\Cetane_Sept26_thresh0.5_dist_diff.csv", delimiter=",", skiprows=0, usecols=[0])

jules1_2 = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\Jules1-2_Sept26_thresh0.5_dist_diff.csv", delimiter=",", skiprows=0, usecols=[0])

jules2_2 = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\Jules2-2_Sept26_thresh0.5_dist_diff.csv", delimiter=",", skiprows=0, usecols=[0])

phantom= np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\Phantom_Sept26_thresh0.5_dist_diff.csv", delimiter=",", skiprows=0, usecols=[0])

zorro = np.loadtxt(r"D:\UCT Mechatronics\Fourth Year\EEE4022S - Thesis\AnnotateVariability\data-AnalysisNetwork\Zorro_Sept26_thresh0.5_dist_diff.csv", delimiter=",", skiprows=0, usecols=[0])

cheetahs = [cetane, jules1_2, jules2_2, phantom, zorro]
xy = []
xy_sum = 0

for cheetah in cheetahs:
    for i in range(len(cheetah)):
        xy.append(cheetah[i])
        xy_sum += cheetah[i]
        
print(xy_sum/len(xy))
print(len(xy))
