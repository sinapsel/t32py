import numpy as np
from scipy.integrate import ode
from typing import Optional, Callable, List
from enum import Enum
from Plotter import Plotter

class Consts:
    c: float = 1
    dim: int = 3
    dt: float = 1e-3

class Particle:
    vec = np.ndarray 
    __mass: float
    __position: vec
    __momentum: vec
    __trajectory: np.ndarray
    def __init__(self, p: Optional[np.ndarray] = np.zeros(Consts.dim),
                 pos: Optional[np.ndarray] = np.zeros(Consts.dim),
                 m: float = 1.0):
        self.__mass = m
        self.__position = pos
        self.__momentum = p
        self.__trajectory = None
    def p(self) -> vec: return self.__momentum
    def p2(self) -> float: return self.p().T @ self.p()
    def m(self) -> float:
        return self.__mass
    def r(self) -> vec:
        return self.__position
    def gamma(self) -> float: 
        return np.sqrt(1 + (self.p().T @ self.p())/(self.m()*Consts.c))
    def get_path(self):
        return self.__trajectory
    
    @staticmethod
    def rhs(t, RP, E, H):
        #dp/dt = ..., dx/dt = ...
        x, p = RP[:3], RP[3:]
        dpdt = E(t, x) + np.sqrt(1+np.dot(p,p))*np.cross(p, H(t, x))
        dxdt = p*np.sqrt(1+p@p)
        return np.hstack((dxdt, dpdt))

    def calculate_trajectory(self, T, E, H):
        timeline = np.arange(0, T, Consts.dt)
        self.__trajectory = np.zeros((len(timeline), 4)) 
        self.__trajectory[:,0] = timeline
        solver = ode(Particle.rhs).set_integrator('dopri5')
        solver.set_initial_value(np.hstack((self.r(), self.p())), timeline[0]).set_f_params(E, H)
        i = 0
        while solver.successful() and solver.t < T:
            solver.integrate(solver.t+Consts.dt)
            self.__trajectory[i, 1:] = solver.y[:3]
            self.__position = solver.y[:3]
            self.__momentum = solver.y[3:]
            i+=1

    def plot_on(self, plot: Plotter):
        axs = plot.axis.value
        pth = self.get_path()
        if (len(axs.idx)) == 3:
                plot.ax.plot3D(
                    *[pth[:, axs.idx[i]] for i in range(3)]
                )
        else:
            plot.ax.plot(
                *[pth[:, axs.idx[i]] for i in range(2)]
            )
                