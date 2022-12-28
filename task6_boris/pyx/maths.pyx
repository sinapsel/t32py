# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False

cdef double dot_product(double[:] left, double[:] right) nogil:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]

cdef double dot(double* left, double* right) nogil:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]

cdef double cross_i(double[:] left, double[:] right, int i) nogil:
    cdef double result = 0
    if i == 0:
        result = left[1] * right[2] - left[2] * right[1]
    elif i == 1:
        result = left[2] * right[0] - left[0] * right[2]
    elif i == 2:
        result = left[0] * right[1] - left[1] * right[0]
    else:
        raise NotImplementedError
    return result

cdef void cross_product(double[:] left, double[:] right, double [:] res_mv) nogil:
    res_mv[0] = left[1] * right[2] - left[2] * right[1]
    res_mv[1] = left[2] * right[0] - left[0] * right[2]
    res_mv[2] = left[0] * right[1] - left[1] * right[0]
