#!/usr/bin/python3

from Space import Space
from Fields import EMCollection
from Particles import Particle
from Plotter import Plotter, AXIS
import numpy as np

def main():
    EH = EMCollection.CROSS(3.)
    sp = Space()
    pt = Plotter(AXIS.yzx)
    sp.particles += [Particle(pos = np.array([0,1,1]), m=3.2)]
    sp.EMFields += [EH]

    sp.simulate(5)
    sp.plot_particle_on(pt)
    pt.plot()



if __name__ == '__main__':
    main()