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

folder_list.sort()
file_list.sort()
print('folder: ', folder_list)
print('file: ', file_list)


N = [5,10,25,50,75]
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
    print(f)
    print(file_list[i])

    os.chdir(cwd)



fig, ax = plt.subplots(2)
for i in range(len(c)):
    ax[0].plot(T,c[i],label="L_{}".format(N[i]),lw=1,marker='+')
    ax[1].plot(T,chi[i],label="L_{}".format(N[i]),lw=1,marker='+')

ax[0].set_title("heat capacity")
ax[0].set_ylabel("$c$")

ax[1].set_title("magnetic susceptibility")
ax[1].set_ylabel("$\chi$")
ax[1].set_xlabel("T")

for axis in ax:
    axis.legend()

plt.tight_layout()
plt.savefig('comparison.png',dpi=300)



