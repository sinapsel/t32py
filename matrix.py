import numpy as np
from numbers import Number
from vec import v2, v3

def gen(n: int, p: float) -> np.ndarray:
    return (np.random.random((n,n)) <= p).astype(int)

def print(M: np.ndarray) -> None:
    print(M)

def _here(pos: v2):
    return tuple(map(lambda x: [x,], list(pos)))

def dfs(M: np.ndarray, pos: v2) -> bool:
    if (pos.y == (M.shape[1] - 1)) and (M[_here(pos)] == 1): #got end
        #print(f'end at {pos}')
        return True
    for i, x_i in enumerate(pos):
        if (x_i < 0 or x_i >= M.shape[i]):
            return False
    # if (pos.x < 0 or pos.x >= M.shape[0]) or (pos.y < 0 or pos.y >= M.shape[1]):
    #     #print(f'bad coords {pos}')
    #     return False
    if M[_here(pos)] <= 0:
        #print(f'at {pos} is {M[pos.x, pos.y]}')
        return False
    M[_here(pos)] = -1 #mark as visited
    return sum([dfs(M, pos + v2.ey), dfs(M, pos - v2.ex), dfs(M, pos + v2.ex)]) > 0

def rfs(M: np.ndarray) -> bool:
    M1 = np.copy(M)
    return sum([dfs(M1, v2.ex * i) for i in range(M.shape[0])]) > 0
    