# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False
from maths cimport dot_product
from libc.math cimport sqrt, sin, cos

cdef class EMF:
    def __init__(self, int parameter, magnitude):
        self.parameter = parameter
        self.k = (0, 0, 1)
        self.k_mv = self.k
        self.magnitude = magnitude
        if self.parameter == 0:
            self.frequency = 0.0
        elif self.parameter == 1:
            self.phase = 0.0
            self.frequency = sqrt(dot_product(self.k_mv, self.k_mv))
            for i in range(3):
                self.k[i] /= self.frequency


    cdef double e(self, double[:] x, double t, int k) nogil:
        cdef double res, res0

        if self.parameter == 0:
            res = 0
        elif self.parameter == 1:
            if k == 0:
                res = cos(self.frequency * t - dot_product(self.k_mv, x) + self.phase)
            elif k == 1:
                res = sin(self.frequency * t - dot_product(self.k_mv, x) + self.phase)
            elif k == 2:
                res = 0
        res0 = res*self.magnitude
        return res0

    cdef double h(self, double[:] x, double t, int k) nogil:
        cdef double res, res0

        if self.parameter == 0:
            if k == 0 or k == 1:
                res = 0
            elif k == 2:
                res = 1
        elif self.parameter == 1:
            if k == 0:
                res = -self.k_mv[2]*sin(self.frequency * t - dot_product(self.k_mv, x) + self.phase)
            elif k == 1:
                res =  self.k_mv[2]*cos(self.frequency * t - dot_product(self.k_mv, x) + self.phase)
            elif k == 2:
                res = self.k_mv[0]*sin(self.frequency * t - dot_product(self.k_mv, x) + self.phase) \
                      - self.k_mv[1]*cos(self.frequency * t - dot_product(self.k_mv, x) + self.phase)
        res0 = res*self.magnitude
        return res0