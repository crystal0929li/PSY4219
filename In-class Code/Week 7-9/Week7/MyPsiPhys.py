import numpy as np
import matplotlib.pyplot as plt


# %%

def psiphys(x      : np.ndarray,
            *,
            alpha  : float =  1.,
            beta   : float =  2.,
            gam    : float = .5,
            lam    : float = .1) -> np.ndarray :
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
    F = 1 - np.exp(-(x / alpha) ** beta)
    psi = gam + (1. - lam - gam) * F
    return (psi)


# %%

x = np.arange(0, 5, .01)
psi1 = psiphys(x)
psi2 = psiphys(x, lam=.2, gam=.4)


# %%

plt.plot(x, psi1, 'r-', x, psi2, 'g-')
plt.xlabel("stimulus manipulation")
plt.ylabel("accuracy")
plt.title("psychophysical function")
plt.ylim((.3, 1))
plt.show()
