import numpy as np
import matplotlib.pyplot as plt



corr = np.loadtxt('autocorr.dat')[:500]
step = range(len(corr))
'''
plt.plot(step,corr)
plt.xlabel('steps')
plt.ylabel('$\chi_{auto}$')
plt.title('magnetization autocorrelation')
plt.savefig('autocorr.png',dpi=150)
'''
corr_log = np.log(corr)
plt.plot(step,corr_log)
plt.xlabel('steps')
plt.ylabel('$log(\chi_{auto})$')
plt.title('log of magnetization autocorrelation')
plt.savefig('autocorr_log.png',dpi=150)
