import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class PlotTrajectory:
    __slots__ = ['x', 't']

    def __init__(self, t: np.ndarray, x: np.ndarray):
        self.t = t
        self.x = x

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        z = self.x[:, 2]
        y = self.x[:, 1]
        x = self.x[:, 0]

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        ax.plot3D(x, y, z, color='coral')

        plt.tight_layout()
        plt.show()

class PlotSpectrum:
    def __init__(self, omg: np.ndarray, spct: np.ndarray):
        self.omg = omg
        self.spct = spct

    def draw(self):
        plt.plot(self.omg, self.spct, c='coral')

        plt.xlabel(r'$\omega$')
        plt.ylabel(r'$\frac{dE}{d\Omega d\omega}$')
        plt.grid()
        # plt.legend()

        plt.tight_layout()
        plt.savefig('spec.svg')
        plt.show()

class PlotDiagramm:
    def __init__(self, X: np.ndarray, Y: np.ndarray, HM):
        self.X = X
        self.Y = Y
        self.heatmap = HM
    
    def draw(self):
        plt.subplot(projection="polar")
        plt.grid(False)
        plt.pcolormesh(self.Y, self.X, self.heatmap)
        #plt.grid()
        plt.colorbar()
        plt.tight_layout()
        plt.savefig('diag.png')
        plt.show()