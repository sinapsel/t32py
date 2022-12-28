# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False
import numpy as np
cimport numpy as np
from libc.math cimport sqrt, sin, cos
from particle cimport Particle
from maths cimport dot_product
from cython.parallel import prange, parallel


cpdef spectrum_calculation(np.ndarray t, np.ndarray x, np.ndarray p, np.ndarray v, np.ndarray direction, tuple omg_span, int nOmg, Particle ptcl):
    cdef:
        int i, j, k, stp
        double n[3]

        double dt
        double Xi, ntXi, dXi, averXi

        double dV[3]
        double averV[3]

        double nrealInteg
        double nimagInteg
        np.ndarray realInteg
        np.ndarray imagInteg
        double[:] realInteg_mv
        double[:] imagInteg_mv

        double[:] n_mv
        double[:] t_mv
        double[:, :] x_mv
        double[:, :] p_mv
        double[:, :] v_mv

        double[:] omg_mv
        double[:] res_mv

        double PI


    n = direction
    PI = np.pi
    n_mv = n
    dt = sqrt(dot_product(n_mv, n_mv)) # abs(n), dt is reused for optimization
    for i in range(3):
        n[i] /= dt

    dt = t[1] - t[0]
    omg = np.linspace(omg_span[0], omg_span[1], nOmg)
    res = np.zeros(nOmg)
    realInteg = np.zeros((3))
    imagInteg = np.zeros((3))

    realInteg_mv = realInteg
    imagInteg_mv = imagInteg
        
    t_mv = t
    x_mv = x
    p_mv = p
    v_mv = v

    omg_mv = omg
    res_mv = res
    stp = t.size - 2
    nOmg = nOmg - 1
    with nogil:
        for j in prange(0, nOmg, num_threads=4):
            for k in range(3):
                realInteg_mv[k] = 0
                imagInteg_mv[k] = 0
            for i in range(0, stp):
                Xi = t_mv[i] - dot_product(n_mv, x_mv[i, :])
                ntXi = t_mv[i+1] - dot_product(n_mv, x_mv[i+1, :])
                dXi = ntXi - Xi
                averXi = 0.5 * (ntXi + Xi)
                for k in range(3):
                    dV[k] = v_mv[i+1, k] - v_mv[i, k]
                    averV[k] = 0.5 * (v_mv[i+1, k] + v_mv[i, k])

                for k in range(3):
                    realInteg_mv[k] += (dt/dXi) * ( 2*averV[k]*sin( omg_mv[j]*dXi*0.5 )*cos ( omg_mv[j]*averXi )
                                                - 2*dV[k]*sin( omg_mv[j]*dXi*0.5 )/omg_mv[j]/dXi*sin( omg_mv[j]*averXi )
                                                - dV[k]*cos( omg_mv[j]*dXi*0.5 )*sin( omg_mv[j]*averXi ) )
                    imagInteg_mv[k] += (dt/dXi) * ( 2*averV[k]*sin( omg_mv[j]*dXi*0.5 )*sin( omg_mv[j]*averXi )
                                                    - 2*dV[k]*sin( omg_mv[j]*dXi*0.5 )/omg_mv[j]/dXi*cos ( omg_mv[j]*averXi )
                                                    - dV[k]*cos(omg_mv[j] * dXi * 0.5)*cos ( omg_mv[j]*averXi ) )
            nrealInteg = dot_product(n_mv, realInteg_mv)
            nimagInteg = dot_product(n_mv, imagInteg_mv)
            res_mv[j] = dot_product(realInteg_mv, realInteg_mv) + dot_product(imagInteg_mv, imagInteg_mv) - nrealInteg**2 - nimagInteg**2
            res_mv[j] *= (0.5 * ptcl.q * omg_mv[j] / PI) ** 2
    return omg, res