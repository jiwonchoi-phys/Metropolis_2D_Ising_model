'''
Code for plotting time-displaced autocorrelation function
'''

import numpy as np
import matplotlib.pyplot as plt

filename = '3D_Ising_N10_J1_T5.80_iter15000.dat'

data = np.loadtxt(filename)
N=75**2
T= float(filename.split('_')[4][1:])
x = data[:500,0]
M_tot = data[:,1]

M = [m for m in M_tot]

def autocorr(M):
	t_max = len(M)
	result = []
	for t in range(t_max):
		corr = np.sum(np.multiply(M[:t_max-t],M[t:t_max]))/(t_max-t) - \
			np.sum(M[:t_max-t])*np.sum(M[t:t_max])/(t_max-t)**2

		result.append(corr)
		print(corr)
	return result

y = autocorr(M)
corr_max = np.max(y)
y = [a/corr_max for a in y]
np.savetxt(fname='autocorr.dat',X=y)


