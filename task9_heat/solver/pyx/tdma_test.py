from sys import path
path.append('.')
from tdma import solve
import numpy as np

import unittest

class TestTDMA(unittest.TestCase):
    def test1(self):
        M = np.array(
            [
                [0, -1, -1, -1],
                [4, 4, 4, 4],
                [-1, -1, -1, 0]
            ],
            dtype=np.float64
        )
        a, b, c = map(lambda arr: arr.reshape((M.shape[1],)), np.split(M, M.shape[0]))
        d = np.array([5, 5, 10, 23], dtype=np.float64)

        actual = np.asarray(solve(a,b,c,d))
        excepted = np.array([2, 3, 5, 7], dtype=np.float64)

        self.assertTrue(
            np.array_equal(
                actual,
                excepted,
                equal_nan=True
            )
        )
    
    def test2(self):
        M = np.array(
            [
                [0, 8, 2, 1.5],
                [4, 18, 5, 1.75],
                [8, 2, 1.5, 0]
            ],
            dtype=np.float64
        )
        a, b, c = map(lambda arr: arr.reshape((M.shape[1],)), np.split(M, M.shape[0]))
        d = np.array([8, 18, 0.5, -1.75], dtype=np.float64)

        actual = np.asarray(solve(a,b,c,d))
        excepted = np.array([0, 1, 0, -1], dtype=np.float64)

        self.assertTrue(
            np.array_equal(
                actual,
                excepted,
                equal_nan=True
            )
        )
        


if __name__ == '__main__':
    unittest.main()