import numpy as np
from scipy.linalg import *
import matplotlib.pyplot as plt

c = 0.5
a = (1 - np.sqrt(c)) ** 2
b = (1 + np.sqrt(c)) ** 2
p = 1000
n = int(p / c)
X = np.random.normal(0, 1, (p, n))
lams, vecs = np.linalg.eigh(X @ X.T / n)


def mc(x):
    # should add (1-1/c)_+ when x = 0
    return 1 / (2 * np.pi * c * x) * np.sqrt((b - x) * (x - a))


x = np.arange(a, b, 0.01)
plt.hist(lams, bins=40, density=True)
plt.plot(x, mc(x), '-', linewidth=3)
plt.show()
ftype = "pdf"
plt.savefig("img/mp." + ftype,
            transparent=True, format=ftype)
