# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:33:52 2020

@author: jiwon
"""

'2D_Ising_N50_J1_T1.10_iter10000.png'

import numpy as np
import matplotlib.pyplot as plt
import sys,os
'''
data_list =[]
filename = sys.argv[0]
N = sys.argv[1]
T = float(filename.split('_')[4][1:])


N=2500
folder='./'
for filename in os.listdir(folder):
    ext=filename.split('.')[-1]
    if ext == 'dat' and filename[0:8] == '2D_Ising':
        data_list.append(filename)
'''

data = np.loadtxt('2D_Ising_N50_J1_T2.32_iter15000.dat')
N=2500
T=2.32
x = data[:,0]
M_tot = data[:,1]
E_tot = data[:,2]



M = [m/N for m in M_tot]
E = [e/N for e in E_tot]


ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)

ax1.plot(x,M,label='T={}'.format(T),lw=0.3)
ax1.set_ylabel('$M_{tot}/N^2$')
ax1.legend(loc="upper right")

ax2.plot(x,E,label='T={}'.format(T),lw=0.3)
ax2.set_xlabel("steps")
ax2.set_ylabel("$E_{tot}/N^2$")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.show()
plt.savefig(filename.split('.')[0]+'.png',dpi=500)