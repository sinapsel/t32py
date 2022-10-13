import numpy as np
from matrix import rfs, gen
from tqdm import tqdm
from typing import Optional
from typing import NamedTuple

class Axis(NamedTuple):
    start: float
    end: float
    step: float

default_nvalues = (10, 15, 20)
'''
defualt values for plottion P_cond at 3 different sizes
'''


def pcond(n: int, p: float, dim: int, k: Optional[int] = None) -> float:
    '''
    evaluate P_cond value
    '''
    if not isinstance(k, int) or k < 0:
        k = 1000
    if not isinstance(n, int) or n <= 0 or not isinstance(p, float) or p < 0 or p > 1:
        raise ValueError
    return sum([rfs(gen(dim, n, p)) for i in tqdm(range(k), desc=f'evaluating for p = {p:.3f}')])/k

def run(dim: int, nvalues = Optional[tuple], density: Optional[int] = None, k: Optional[int] = None) -> None:
    '''
    run the experiment of path finding and save to txt file
    '''
    if nvalues == None:
        nvalues = default_nvalues
    if density == None:
        density = 25
    ax = Axis(start = 0, end = 1, step = density)
    for i in nvalues:
        with open(f"data{i}.txt", "w") as f:
            for p in np.linspace(*ax):
                f.write('%7.4f\t%7.4f\n'%(p, pcond(i, p, dim, k)))