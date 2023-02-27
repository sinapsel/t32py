from solver import solver, jacobi
import numpy as np

U0 = 100.0
h = 1.0
sizes = solver.Sizes(
        x = solver.Interval(0, 40), y = solver.Interval(0, 40)
    )
nsx = int((sizes.x.end - sizes.x.start )/h)
nsy = int((sizes.y.end - sizes.y.start )/h)

bm = np.zeros((nsx, nsy)).astype(bool)
bm[0,:] = True
bc = np.zeros((nsx, nsy))
np.putmask(bc, bm, U0)

js = jacobi.JacobiSolver(
    sizes=sizes,
    dh = h,
    rtol = 1e-1
)
js.set_bounds(bm, bc)
#print(js.axis_x)
#print(js.map)


z = js.run()
from plotter import plotAll
plotAll(js.axis_x, js.axis_y, z, fname='t01j.png')
