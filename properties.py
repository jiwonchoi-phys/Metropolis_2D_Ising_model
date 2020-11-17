import numpy as np
import sys, os

cwd = os.getcwd()
folder = cwd+'/'+'2D_N75'

os.chdir(folder)

file_list = []
M_list = []
E_list = []
T_list = []
c_list = []
chi_list = []
output = []

for filename in os.listdir(os.getcwd()):
    if filename[:2] == '2D':
        file_list.append(filename)

for f in file_list:
    data = np.loadtxt(f)
    T = float(f.split('_')[4][1:])
    N = int(folder[-2:])
    
    M = data[-10000:,1]
    M = [m/N**2 for m in M]
    
    E = data[-10000:,2]
    #E = [e/N**2 for e in E]

    M2 = np.power(M,2)
    E2 = np.power(E,2)

    mavg = np.mean(M)
    eavg = np.mean(E)

    c = (np.mean(E2) - np.power(eavg,2))/(T**2*N)
    chi = (np.mean(M2) - np.power(mavg,2))*N/T
    
    M_list.append(mavg)
    E_list.append(eavg)
    T_list.append(T)
    c_list.append(c)
    chi_list.append(chi)

print(c_list)

for i in range(len(T_list)):
    output.append([T_list[i],M_list[i],E_list[i],c_list[i],chi_list[i]])

np.savetxt(fname='N{}_output.dat'.format(N),X=output,\
    header='T        m        E       c       chi')
