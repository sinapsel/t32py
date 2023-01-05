from enum import Enum
from matplotlib import animation, pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Tuple, Optional

class AX:
    labels: Tuple[str]
    units: Tuple[str]
    idx: Tuple[int]
    def __init__(self, labels : Tuple[str], units: Tuple[str], idx: Tuple[int]) -> None:
        self.labels = labels
        self.units = units
        self.idx = idx


class AXIS(Enum):
    tx: AX = AX(('t', 'x'), (r', $\frac{\alpha}{mc^3}$', r', $\frac{\alpha}{mc^2}$'), (0, 1))
    ty: AX = AX(('t', 'y'), (r', $\frac{\alpha}{mc^3}$', r', $\frac{\alpha}{mc^2}$'), (0, 2))
    tz: AX = AX(('t', 'z'), (r', $\frac{\alpha}{mc^3}$', r', $\frac{\alpha}{mc^2}$'), (0, 3))

    xy: AX = AX(('x', 'y'), (r', $\frac{\alpha}{mc^2}$', r', $\frac{\alpha}{mc^2}$'), (1, 2))
    yz: AX = AX(('y', 'z'), (r', $\frac{\alpha}{mc^2}$', r', $\frac{\alpha}{mc^2}$'), (2, 3))
    zx: AX = AX(('z', 'x'), (r', $\frac{\alpha}{mc^2}$', r', $\frac{\alpha}{mc^2}$'), (3, 1))

    xyz: AX = AX(('x', 'y', 'z'), (r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$'), (1, 2, 3))
    zxy: AX = AX(('z', 'x', 'y'), (r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$'), (3, 1, 2))
    yzx: AX = AX(('y', 'z', 'x'), (r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$',r', $\frac{\alpha}{mc^2}$'), (2, 3, 1))


class Plotter(object):
    axis: AXIS
    def __init__(self, axis: AXIS) -> None:
        self.axis: AXIS = axis
        self.fig = plt.figure()
        if (len(self.axis.value.idx) == 3):
            self.ax: Axes3D = self.fig.add_subplot(111, projection='3d')
        else:
            self.ax = self.fig.add_subplot(111)

    
    def plot(self, fname: Optional[str] = 'out.png'):
        self.ax.set_xlabel(self.axis.value.labels[0] + self.axis.value.units[0])
        self.ax.set_ylabel(self.axis.value.labels[1] + self.axis.value.units[1])
        if (len(self.axis.value.idx) == 3):
            self.ax.set_zlabel(self.axis.value.labels[2] + self.axis.value.units[2])
        self.fig.savefig(fname)
