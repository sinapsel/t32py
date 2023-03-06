import sys
sys.path.append('./solver/lib/')
from .solver import ISolver, np
from relaxation import relaxation

class Solver(ISolver):
    def run(self, omega):
        z, _, _ = relaxation(self.bound_values,self.bound_map, 1e-2, self.dh, omega)
        return np.asarray(z)