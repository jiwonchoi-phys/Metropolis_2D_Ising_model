import numpy as np
import matplotlib.pyplot as plt
import sys,os

folder = 'D:/python/Ising/N50_J1'
os.chdir(folder)

data_list = []
slice_num = 3000
N = 2500


for filename in os.listdir(folder):
    ext=filename.split('.')[-1]
    if ext == 'dat' and filename[0:8] == '2D_Ising':
        data_list.append(filename)

def plot_m(show=False):
    T_list = []
    M_mean = []
    M_stdev = []

    for file in data_list:
        
        data = np.loadtxt(file)
        T = float(file.split('_')[4][1:])
        
        M = [m/2500 for m in data[-slice_num:,1]]
        avg = np.mean(M)
        std = np.std(M)
        
        T_list.append(T)
        M_mean.append(avg)
        M_stdev.append(std)

    plt.errorbar(T_list,M_mean,M_stdev,fmt='o',color='black',capsize=2,\
        markersize=5)
    plt.title("$N$={}, $J=1$, Magnetization".format(N))
    plt.xlabel("T")
    plt.ylabel("$<m>$")
    plt.ylim(-0.1,1.05)
    
    if show == True:
        plt.show()
    
    plt.savefig('magnetization.png', dpi=350)
        

def plot_c(show=False):
    T_list=[]
    c_list=[]
    
    for file in data_list:
        
        data = np.loadtxt(file)
        T = float(file.split('_')[4][1:])
        
        E = data[-slice_num:,2]
        E_pow = np.power(E,2)
        avg = np.mean(E)
        avg_pow = np.mean(E_pow)
        
        c = (avg_pow-np.power(avg,2))/(N*T**2)
        
        
        T_list.append(T)
        c_list.append(c)

    plt.scatter(T_list,c_list,color='black',marker='+')
    plt.title("$N$={}, $J=1$, Heat capacity".format(N))
    plt.xlabel("T")
    plt.ylabel("$c$")
    
    if show == True:
        plt.show()  
            
    plt.savefig('heat_capacity.png', dpi=350)

def plot_chi(show=False):
    T_list=[]
    M_list=[]
    
    for file in data_list:
        
        data = np.loadtxt(file)
        T = float(file.split('_')[4][1:])
        
        M = data[-slice_num:,1]
        M_pow = np.power(M,2)
        avg = np.mean(M)
        avg_pow = np.mean(M_pow)
        
        M = (avg_pow-np.power(avg,2))*N/T
        
        
        T_list.append(T)
        M_list.append(M)

    plt.scatter(T_list,M_list,color='black',marker='+')
    plt.title("$N$={}, $J=1$, Magnetic Susceptibility".format(N))
    plt.xlabel("T")
    plt.ylabel("$\chi$")
    
    if show == True:
        plt.show()
        
    plt.savefig('Magnetic_susceptibility.png', dpi=350)

plot_c()


'''
data = np.loadtxt('magnetization.dat')
T = data[:,0]
M = np.abs(data[:,1])
M = [m/2500 for m in M]

plt.scatter(T,M,c='black',marker='+')
plt.xlabel("T")
plt.ylabel("<m>")
plt.savefig('M.png',dpi=350)
'''