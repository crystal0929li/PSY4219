#
# test calling psiphys module
#

import numpy as np
import matplotlib.pyplot as plt
import PsiPhys

x = np.arange(0, 5, .01)
psi1 = PsiPhys.psiphys(x, lam=.1, gam=.6)
psi2 = PsiPhys.psiphys(x, lam=.2, gam=.4)

plt.plot(x, psi1, 'r-', x, psi2, 'g-')
plt.xlabel("stimulus manipulation")
plt.ylabel("accuracy")
plt.title("psychophysical function")
plt.ylim((.3, 1))
plt.show()
