from .solver import ISolver, np
class Solver(ISolver):
    def run(self):
        it = 0
        rel_res = 1.0

        U = self.map
        dh = self.dh
        dt = self.dt
        al = dt/(dh*dh)
        U1 = 1000
        itmax = U.shape[1]
        rtol = 1e-5
        while (rel_res>rtol) and (it+1<itmax):
            dU = al * (U[2:, it] + U[0:-2, it] - 2*U[1:-1, it])
            it += 1    
            U[1:-1, it] = U[1:-1, it - 1] + dU
            # U = U*(~self.bound_map) + self.bound_values
        return U
        
