#HIGH
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = 1/x
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$f_r$")
plt.xlabel("$r$")
plt.plot(x, y, "k--", label = "$\\frac{1}{r}$")
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('2.pdf', format="pdf")
plt.savefig('2.png', format="png")