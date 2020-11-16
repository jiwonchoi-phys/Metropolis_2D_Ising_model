import numpy as np
import matplotlib.pyplot as plt
import sys,os

Tc = 2.269
gamma = 7/4
nu = 1

folder_list = []
file_list = []
for folder in os.listdir(os.getcwd()):
    if os.path.isdir(folder) and folder[0:2] == '2D':
        folder_list.append(folder)    
    


for folder in folder_list:
    for filename in os.listdir(os.getcwd()+'/'+folder):
        if filename[:5] == 'equil':
            file_list.append(filename)


for i in range(len(folder_list)):
    os.chdir(get.cwd()+'/'+folder[i])
    data = np.loadtxt(file_list[i])
    N = filename.split('.')[0][-2:]
    T = data[:,0]
    t = abs(T/Tc-1)
    chi0 = data[]





