"""
Implementation of 2D square lattice Ising model
Author : Jiwon Choi
"""

import numpy as np
import matplotlib.pyplot as plt


class Ising2D():
    def __init__(self,N,J,T,steps):
        self.N = N
        self.J = J
        self.T = T
        self.steps = steps
        self.grid = self.make_grid()
    
        self.M = self.total_M()
        self.E = self.total_E()
        self.M_list = []
        self.E_list = []
        
    def make_grid(self):
        return np.random.choice([1,-1],size=[self.N,self.N])

    
    def return_grid(self):
        return self.grid
    
    
    def total_M(self):
        return np.sum(self.grid)
    
    
    def E_ij(self,i,j):
        # Energy with periodic boundary condition
        E_ij = -self.J * self.grid[i,j] * \
            (self.grid[(i+1)%self.N,j] + self.grid[(i-1)%self.N,j] + \
             self.grid[i,(j-1)%self.N] + self.grid[i,(j+1)%self.N])
        
        return E_ij
    
    
    def total_E(self):
        E_tot = 0
        for i in range(self.N):
            for j in range(self.N):
                E_tot += self.E_ij(i,j) 
        
        return E_tot
    
    
    def dE(self,i,j):
        dE_ij = 2 * self.J * self.grid[i,j] * \
            (self.grid[(i+1)%self.N,j] + self.grid[(i-1)%self.N,j] + \
             self.grid[i,(j-1)%self.N] + self.grid[i,(j+1)%self.N])
                
        return dE_ij
    
    
    def step(self):
        
        # Choose random site i,j
        i = np.random.randint(self.N)
        j = np.random.randint(self.N)
        p = np.random.uniform(0,1)
        
        # Calculate energy difference
        dE = self.dE(i,j)
        
        # Metropolis algorithm
        if dE < 0:
            self.grid[i,j] *= -1
            self.M += 2*self.grid[i,j]
            self.E += dE
            
        elif dE > 0 and p < np.exp(-dE/self.T):
            self.grid[i,j] *= -1
            self.M += 2*self.grid[i,j]
            self.E += dE
    
    
    def run(self,log=None):
        proceed=0
        print("\n\nINPUT PARAMETER")
        print('(N={}, J={}, T={}, steps={})'.format(self.N,self.J,self.T,self.steps))
        print('\nSimulation started.\n')
        for i in range(self.steps):
            for j in range(self.N**2):
                self.step()
            self.M_list.append(self.M)
            self.E_list.append(self.E)
            proceed += 1
            if proceed % log == 0:
                print('    Steps:{}, M:{}, E:{}'.format(proceed,self.M,self.E))
        print('\nSimulation ended.')
    
    def savedata(self):
        filename = '2D_Ising_N{}_J{}_T{}_steps{}.dat'.format(self.N,self.J,self.T,self.steps)
        header = '2D Ising model simulation with metropolis algorithm \n'+\
            '(N={}, J={}, T={}, steps={})\n'.format(self.N,self.J,self.T,len(self.M_list))+\
            'steps    M      T'
        x = np.arange(len(self.M_list))
        data = np.array([x, self.M_list, self.E_list]).transpose()
        np.savetxt(fname=filename,X = data, fmt = '%.10e', header=header)
    
    
    def plot(self,save=True):
        x = np.arange(len(self.M_list))
        M = [m/self.N**2 for m in self.M_list]
        E = [e/self.N**2 for e in self.E_list]
        
        ax1 = plt.subplot(2,1,1)
        ax2 = plt.subplot(2,1,2)
        
        ax1.plot(x,M,label='T={}'.format(self.T),lw=0.5,c='black')
        ax1.set_ylabel('$M_{tot}/N^2$')
        ax1.legend(loc="upper right")
        
        ax2.plot(x,E,label='T={}'.format(self.T),lw=0.5,c='black')
        ax2.set_xlabel("steps")
        ax2.set_ylabel("$E_{tot}/N^2$")
        ax2.legend(loc="upper right")
        
        
        plt.tight_layout()
        plt.show()
        
        if save == True:
            filename = '2D_Ising_N{}_J{}_T{}_steps{}.png'.format(self.N,self.J,self.T,self.steps)
            plt.savefig(filename, dpi=350)
            

if __name__ == "__main__":
    N = int(input("# Input N(for N*N square lattice): "))
    J = float(input("# Input interaction constant J: "))
    T = float(input("# Input temperature T: "))
    steps = int(input("# Input number of simulation of each site: "))
    
    model = Ising2D(N,J,T,steps)
    grid_i = model.return_grid()
    
    model.run(log=100)
    model.savedata()
    model.plot()
    
    grid_f = model.return_grid()
    
    
    
