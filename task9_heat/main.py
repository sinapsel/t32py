#!/usr/bin/env pytdhon3

from solver import *
import numpy as np

T0 = 100.0
dh = 0.5
dt = 0.1
space = solver.Space(
        x = solver.Interval(0, 10), t = solver.Interval(0, 45)
    )
nsx = int((space.x.end - space.x.start )/dh)
nst = int((space.t.end - space.t.start )/dt)

bm = np.zeros((nsx, nst)).astype(bool)

bm[0, :] = True
bm[-1, :] = True
bm[:, 0] = True

bc = np.zeros((nsx, nst))
bc[0, :] = 0
bc[-1, :] = 0
bc[:, 0] = T0
bc[:, 0] = np.sin(np.pi*(np.mgrid[space.x.start:space.x.end:dh])/space.x.end) # eigenfunction initial condition

js = eftcs.Solver(
    space=space,
    dh = dh,
    dt = dt,
    rtol = 1e-1
)
# js = gauss_seidel.Solver(
#     space=space,
#     ddh = dh,
#     rtol = 1e-1
# )
js.set_bounds(bm, bc)
#print(js.axis_x)
#print(js.map)


z = js.run()

from plotter import plotAll
plotAll(js.axis_x, js.axis_t, z, fname='t01j.png')
