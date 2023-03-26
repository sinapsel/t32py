from .solver import ISolver, np

class Solver(ISolver):
    def run(self):
        u = self.map
        dt = self.dt
        dx = self.dh
        V = self.V

        u[1:-1, 1] = u[1:-1, 0] + (1j)*dt*(u[2:, 0] - 2*u[1:-1, 0] + u[:-2, 0])/(dx*dx) - 1j*dt*V[1:-1]*u[1:-1, 0]
        u[0, 1] = u[0,0]+(1j)*dt*(u[1,0] - 2*u[0,0])/dx**2 - 1j*dt*V[0]*u[0,0]
        u[-1, 1] = u[-1, 0]+dt*(1j)*( -2*u[-1, 0] +u[-2, 0])/dx**2 - 1j*dt*V[-1]*u[-1, 0]

        for t in range(2, len(u[0, :])):
            u[1:-1, t] = ((2j*dt/(dx**2.0))*(u[2:, t-1] + u[:-2, t-1] - u[1:-1, t-2]) + -2j*dt*V[1:-1]*u[1:-1, t-1] + u[1:-1, t-2])/(1.0+2j*dt/dx**2.0)
            u[0, t] = ((2j*dt/dx**2.0)*(u[1, t-1] - u[0,t-2]) + -2j*dt*V[0]*u[0,t-1] + u[0,t-2])/(1.0+2j*dt/dx**2.0)            
            u[-1, t] = ((2j*dt/dx**2.0)*(u[-2,t-1] - u[-1,t-2]) + -2j*dt*V[-1]*u[-1,t-1] + u[-1,t-2])/(1.0+2j*dt/dx**2.0)

            u[:, t] /= np.sqrt(np.sum(np.abs(u[:,t])**2))


        return u.copy()