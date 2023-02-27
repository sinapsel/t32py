# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False


cdef class Particle:
    cdef:
        double q, m
        double[:] x0, p0