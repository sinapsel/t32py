# cython: language_level=3str

cdef class EMF:
    cdef:
        int parameter

        double frequency
        double magnitude
        double phase
        double k[3]
        double[:] k_mv

    cdef double e(self, double[:] x, double t, int j) nogil
    cdef double h(self, double[:] x, double t, int j) nogil