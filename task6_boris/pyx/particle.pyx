# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False


cdef class Particle:
    def __init__(self, double q, double m, double[:] x0, double[:] p0):
        self.q = q
        self.m = m
        self.x0 = x0
        self.p0 = p0