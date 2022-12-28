# cython: language_level=3str, boundscheck=False, wraparound=False, cdivision=True, initializedcheck=False
import numpy as np
cimport numpy as np
from cython.parallel import prange, parallel
from libc.math cimport sqrt, sin, cos
from maths cimport dot_product, cross_i
from emf cimport EMF
from particle cimport Particle

cpdef tuple boris_push(ptcl: Particle, field: EMF, t_span: tuple, nt: int, react: bool):
    cdef:
        int i, k, swtch, stp
        double scaling, K, dt, temp = 0

        double p_plus[3]
        double p_minus[3]
        double p_prime[3]

        double tau[3]
        double sigma[3]

        double xtmp[3]
        double averV[3]

        double currE[3]
        double currH[3]

        double[:] t_mv
        double[:, :] x_mv
        double[:, :] p_mv
        double[:, :] v_mv

        double[:] p_minus_mv
        double[:] p_prime_mv

        double[:] tau_mv
        double[:] sigma_mv

        double[:] averV_mv

        double[:] currE_mv
        double[:] currH_mv

    t = np.linspace(t_span[0], t_span[1], nt)
    x = np.zeros((nt, 3), dtype=np.double)
    p = np.zeros((nt, 3), dtype=np.double)
    v = np.zeros((nt, 3), dtype=np.double)
    swtch = react
    stp = nt


    t_mv = t
    x_mv = x
    p_mv = p
    v_mv = v

    dt = t[1] - t[0]
    scaling = field.frequency * ptcl.q ** 2 / ptcl.m
    K = 0

    x[0, :] = ptcl.x0
    p[0, :] = ptcl.p0
    for k in range(3):
        v[0, k] = ptcl.p0[k] / sqrt(1+dot_product(p[0, :], p[0, :]))

    p_minus_mv = p_minus
    p_prime_mv = p_prime
    tau_mv = tau
    sigma_mv = sigma
    averV_mv = averV
    currE_mv = currE
    currH_mv = currH

    with nogil:
        for i in range(1, stp):
            for k in range(3):
                currE_mv[k] = field.e(x_mv[i-1, :], t_mv[i], k)
                currH_mv[k] = field.h(x_mv[i-1, :], t_mv[i], k)

            temp = dot_product(p_mv[i-1, :], p_mv[i-1, :])
            for k in range(3):
                tau[k] = currH[k] * dt / 2 / sqrt(1 + temp)
            for k in range(3):
                sigma[k] = 2 * tau[k] / (1 + dot_product(tau_mv, tau_mv))
            for k in range(3):
                p_minus[k] = p_mv[i-1, k] + currE[k] * dt / 2
            for k in range(3):
                p_prime[k] = p_minus[k] + cross_i(p_minus_mv, tau_mv, k)
            for k in range(3):
                p_plus[k] = p_minus[k] + cross_i(p_prime_mv, sigma_mv, k)
            for k in range(3):
                p_mv[i, k] = p_plus[k] + currE[k] * dt / 2

            for k in range(3):
                averV[k] = (p_mv[i, k] + p_mv[i-1, k]) / 2 / sqrt(1 + temp)
            for k in range(3):
                sigma[k] = currE[k] + cross_i(averV_mv, currH_mv, k)
                K = (1 + temp) * swtch  * 1.18e-8 * scaling * (dot_product(sigma_mv, sigma_mv) - (dot_product(averV_mv, sigma_mv)) ** 2)  # letter K
            for k in range(3):
                p_mv[i, k] = p_mv[i, k] - dt * K * averV[k]
            for k in range(3):
                x_mv[i, k] = x_mv[i-1, k] + p_mv[i, k] * dt / sqrt(1 + temp)
            for k in range(3):
                v_mv[i, k] = p_mv[i, k] / sqrt(1 + temp)

    return t, x, p, v
