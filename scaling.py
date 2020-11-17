import numpy as np
import matplotlib.pyplot as plt
import sys,os

Tc = 2.269
gamma = 7/4
nu = 1
cwd = os.getcwd()

folder_list = []
file_list = []
for folder in os.listdir(cwd):
    if os.path.isdir(folder) and folder[0:2] == '2D':
        folder_list.append(folder)    
    


for folder in folder_list:
    for filename in os.listdir(cwd+'/'+folder):
        if filename.split('.')[0][-6:] == 'output':
            file_list.append(filename)

print('folder: ', folder_list)
print('file: ', file_list)


N = [25,50,75]
c = []
chi=[]

for i,f in enumerate(folder_list):
    os.chdir(os.getcwd()+'/'+f)
    data = np.loadtxt(file_list[i])
    
    T = data[:,0]
    t = T/Tc-1
    chi.append(data[:,4])
    c.append(data[:,3])
    print("N: ", N)

    os.chdir(cwd)

fig1 = plt.figure()
fig2 = plt.figure()

for i in range(len(chi)):
    fig1.plot(T,c[i])
    fig2.plot(T,chi[i])
fig1.savefig('c_comp.png',dpi=150)
fig2.savefig('chi_comp.png',dpi=150)



