#
# psychophysical function module
#

import numpy as np
import matplotlib.pyplot as plt


def psiphys(x, alpha=1., beta=2., gam=.5, lam=.1):
    """Computes psychophysical function

    Arguments:
        x (numpy array):   point at which to evaluate psi(x)
        alpha (float):     scale parameter of the Weibull
        beta (float):      shape parameter of the Weibull
        gam (float):       chance (floor on performance)
        lam (float):       lapse rate (ceil on performance)

    Returns:
        psi (numpy array): psychophysical function psi(x)
    """
    F = 1 - np.exp(-(x/alpha) ** beta)
    psi = gam + (1. - lam - gam) * F
    return (psi)


if __name__ == '__main__':
    x = np.arange(0, 5, .01)
    psi = psiphys(x, lam=.05, gam=.4)
    plt.plot(x, psi, 'r-')
    plt.xlabel("stimulus manipulation")
    plt.ylabel("accuracy")
    plt.title("psychophysical function")
    plt.ylim((.4, 1))
    plt.show()
