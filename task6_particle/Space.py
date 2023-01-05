from Particles import Particle
from Fields import ElectromagneticField
from typing import Optional, Callable, List
from Plotter import Plotter

class Space(object):
    particles: List[Particle] = []
    EMFields: List[ElectromagneticField] = []
    def Time(self, dt: float, T = None):
        t = 0
        while (T==None) or t < T:
            yield t
            t += dt
    def __init__(self, particles: Optional[List[Particle]] = [],
                 emfields: Optional[List[Particle]] = []):
          self.particles = particles
          self.EMFields = emfields
        
    def simulate(self, T: float):
        for p in self.particles:
              E = lambda t, r: sum([emfield.E.field(t, r)
                                           for emfield in self.EMFields])
              H = lambda t, r: sum([emfield.H.field(t, r)
                                           for emfield in self.EMFields])
              p.calculate_trajectory(T, E, H)

    def plot_particle_on(self, plot: Plotter):
        for p in self.particles:
            p.plot_on(plot=plot)
