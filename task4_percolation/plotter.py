import matplotlib.pyplot as plt
import numpy as np
from typing import Optional
from data_runner import Axis


_default_axes = Axis(start = 0., end = 1., step = 0.2)

def plot(dim: int, nvalues: Optional[tuple] = None, axes: Axis = None):
    '''
    read data and plot it
    '''
    if nvalues == None:
        nvalues = (10, 15, 20)
    if axes == None:
        axes = _default_axes
    
    fig, ax = plt.subplots(1,1, figsize=(10,6))
    for i in nvalues:
        p, cond = np.genfromtxt(f"data{i}.txt", delimiter="\t", dtype=np.float32).T
        ax.plot(p, cond, 'o-', linewidth=2.0, label=f'$n={i}$')

    ax.set(xlim=(0, 1), xticks=np.arange(*axes),
        ylim=(0, 1), yticks=np.arange(*axes))
    plt.title(f'Percolation for {dim}D')
    plt.xlabel('p')
    plt.ylabel('$P_{cond}$')
    plt.legend(loc='upper left')
    plt.savefig('plot.png', dpi = 120)