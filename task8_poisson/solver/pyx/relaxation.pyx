import cython
cimport cython

import numpy as np
cimport numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)

cpdef relaxation(np.ndarray[np.float64_t, ndim=2] U, double rtol, double h, double omega):
    cdef Py_ssize_t i, j, it
    cdef double rel_res, dU_max, dU, R

    cdef unsigned int rows = U.shape[0]
    cdef unsigned int cols = U.shape[1]
    
    it=0
    rel_res=1.0
        
    itmax=500
    
    while ((rel_res>rtol) and (it<=itmax)):
        dU_max=0.0
        for j in range(1,rows-2):
                for i in range(1,cols-2):
                    R = (U[j,i-1]+U[j-1,i]+U[j,i+1]+U[j+1,i])/4-U[j,i] 
                    dU =  omega*R
                    U[j,i] += dU
                    dU_max=np.max([np.abs(dU),dU_max])
                   
        rel_res=dU_max/np.max(np.abs(U[:,:]))
#         print 'rel_res', rel_res
        it+=1 
    return U