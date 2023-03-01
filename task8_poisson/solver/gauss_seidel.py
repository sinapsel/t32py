import sys
sys.path.append('./lib/')
from .solver import Solver, np
from relaxation import relaxation

class GaussSeidelSolver(Solver):
    def run(self):
        iteration = 0
        rel_res = 1.0

        z = self.map
        h = self.dh
        
        while(iteration < 500):
            #z0 = np.sum(np.square(z))
            z[1:-1, 1:-1] = (z[1:-1,0:-2] + z[0:-2,1:-1] + z[1:-1,2:]+ z[2:,1:-1])/4
            #z1 = np.sum(np.square(z))
            #print(np.abs(z1-z0))
            z = z*(~self.bound_map) + self.bound_values
            iteration += 1    
        return z