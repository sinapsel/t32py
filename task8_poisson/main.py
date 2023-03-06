#!/usr/bin/env python3

from solver import solver, jacobi, gauss_seidel, super_relaxation
import numpy as np

U0 = 100.0
h = 1.0
sizes = solver.Sizes(
        x = solver.Interval(0, 40), y = solver.Interval(0, 40)
    )
nsx = int((sizes.x.end - sizes.x.start )/h)
nsy = int((sizes.y.end - sizes.y.start )/h)

bm = np.zeros((nsx, nsy)).astype(bool)
id = 10
idy = 5
bm[id,idy:-1-idy] = True
bm[-1-id,idy:-1-idy] = True

bc = np.zeros((nsx, nsy))
bc[id, idy:-1-idy] = U0
bc[-1-id, idy:-1-idy] = -U0

js = jacobi.Solver(
    sizes=sizes,
    dh = h,
    rtol = 1e-1
)
# js = gauss_seidel.Solver(
#     sizes=sizes,
#     dh = h,
#     rtol = 1e-1
# )
js.set_bounds(bm, bc)
#print(js.axis_x)
#print(js.map)


z = js.run()
from plotter import plotAll
plotAll(js.axis_x, js.axis_y, z, fname='t01j.png')
