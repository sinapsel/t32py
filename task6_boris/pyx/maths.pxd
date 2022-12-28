# cython: language_level=3str

cdef double dot_product(double[:] left, double[:] right) nogil
cdef double cross_i(double[:] left, double[:] right, int i) nogil