#!/usr/bin/env python
import sys
sys.path.append('./lib/')
from boris_method import boris_push
from emf import EMF
from particle import Particle
from radiation import spectrum_calculation
from plotter import PlotTrajectory, PlotSpectrum, PlotDiagramm
import numpy as np

import matplotlib.pyplot as plt

# Config
nt = 1000
t_span = (0., 100.)

q = 1.
m = 1.
x0 = np.array([0, 0, 0]).astype(np.double)
p0 = np.array([-10.0, 0.0, 0.0]).astype(np.double)
ReactionForce = True

objPtcl = Particle(q, m, x0, p0)
objEMF = EMF(0, 10)

trj = boris_push(objPtcl, objEMF, t_span, nt, ReactionForce)

PlotTrajectory(trj[0], trj[1]).draw()


n = np.array([0, 1, 0]).astype(np.double)
frequencies_bound = (0., 6.28)
freq_dens = 500
spct = spectrum_calculation(trj[0], trj[1], trj[2], trj[3], n, frequencies_bound, freq_dens, objPtcl)

PlotSpectrum(spct[0], spct[1]).draw()


tht_span = (0., 2*np.pi)
nTht = 628

tht = np.linspace(tht_span[0], tht_span[1], nTht)
heatmap = np.zeros((nTht, freq_dens))
for i in range(nTht):
    n[0] = np.sin(tht[i])
    n[1] = 0
    n[2] = np.cos(tht[i])
    heatmap[i][:] = spectrum_calculation(trj[0], trj[1], trj[2], trj[3], n, frequencies_bound, freq_dens, objPtcl)[1][:]
else:
    omg = np.linspace(frequencies_bound[0], frequencies_bound[1], freq_dens)

X, Y = np.meshgrid(omg, tht)

PlotDiagramm(X, Y, heatmap).draw()
