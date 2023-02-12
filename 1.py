import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.linspace(1, 10, 100)
y1 = np.log10(1+1/x)
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$P(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y1, "k--", label='$log_{10}(1+\\frac{1}{\delta})$')
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('1.pdf', format="pdf")
plt.savefig('1.png', format="png")