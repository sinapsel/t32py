import numpy as np
from Plotter import Plotter
from typing import Optional, Callable, List


class Field(object):
    field: Callable[[float, np.ndarray], np.ndarray]
    def __init__(self, field: Callable[[float, np.ndarray], np.ndarray]):
        self.field = field
    def __call__(self):
        return self.field
    # def plot_on(self, plot: Plotter, t=0):
    #     # x, y, z = np.arange(*(*plot.ax.get_xlim(), 0.5)).T, np.arange(*(*plot.ax.get_ylim(), 0.5)).T, np.arange(*(*plot.ax.get_zlim(), 0.5)).T
    #     # fx = self.field(t, np.hstack((x, y, z)))
    #     # for xx in x:
    #     #     for yy in y:
    #     #         for zz in z:

    #     # # dx, dy, dz = np.gradient(fx)
    #     # color = np.sqrt(dx.T@dx + dy.T@dy + dz.T@dz)
    #     # plot.ax.quiver3D(x, y, z, dx, dy,dz, color)


class EField(Field):
    pass

class HField(Field):
    pass

class ElectromagneticField(object):
    def __init__(self, E: EField, H: HField):
        self.E = E
        self.H = H
    def Intencity(self, t, r):
        E2 = self.E.field(t, r); E2 = E2.T @ E2
        H2 = self.H.field(t, r); H2 = H2.T @ H2
        return (E2 + H2)/(4*np.pi)

    def plot_on(self, plot, t=0): pass


class EMCollection:
    CROSS = lambda E: ElectromagneticField(
        EField(
            lambda t, r: np.array([1, 0, 0])*E
        ),
        HField(
            lambda t, r: np.array([0, 1, 0])*E
        )
    )
    STATIC = lambda E, H: ElectromagneticField(
        EField(
            lambda t, r: E
        ),
        HField(
            lambda t, r: H
        )
    )