import numpy as np
from numbers import Number
from vec import vec, v2, v3


def gen(dim: int, n: int, p: float) -> np.ndarray:
    '''
    generate square matrix n x n ... x n dim times. with probability p cell is 1 and (p-1) is 0
    '''
    return (np.random.random((n,)*dim) <= p).astype(int)

def deep_forward(t: type) -> vec:
    '''
    directions for deep-first-search
    '''
    if t is v2:
        yield v2.ey; yield -v2.ex; yield v2.ex
    elif t is v3:
        yield v3.ey; yield -v3.ex; yield -v3.ez; yield v3.ex; yield v3.ez


def _here(pos: vec) -> tuple:
    return tuple(map(lambda x: [x,], list(pos)))

def dfs(M: np.ndarray, pos: vec) -> bool:
    '''
    deep first search at matrix M from position pos
    '''
    if (pos.y == (M.shape[1] - 1)) and (M[_here(pos)] == 1): #got end
        return True
    for i, x_i in enumerate(pos):
        if (x_i < 0 or x_i >= M.shape[i]):
            return False
    if M[_here(pos)] <= 0:
        return False
    M[_here(pos)] = -1 #mark as visited
    return sum([dfs(M, pos + step) for step in deep_forward((v2, v3)[len(M.shape) - 2])]) > 0

def rfs(M: np.ndarray) -> bool:
    '''
    run dfs for every cell in first row
    '''
    M1 = np.copy(M)
    dim = len(M.shape)
    if dim == 2:
        return sum([dfs(M1, v2.ex * i) for i in range(M.shape[0])]) > 0
    if dim == 3:
        return sum([dfs(M1, v3.ex * i + v3.ez*j) for i in range(M.shape[0]) for j in range(M.shape[2])]) > 0
    