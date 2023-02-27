import cython
cimport cython

import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)

cpdef gseidel(np.ndarray[np.float64_t, ndim=2] U, double rtol, double h, double omega):
    cdef:
    	unsigned int rows = U.shape[0]
    cdef unsigned int 
    while(it <= 500)
