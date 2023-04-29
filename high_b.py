import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = np.array([0.229918699, 0.068617886, 0.079349593, 0.067317073, 0.021788618, 0.024715447, 0.030569106, 0.030569106, 0.015934959])
y2 = np.log10(1+1/x)
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$P(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y1, "k--", label='$Actual\ Probability$')
plt.plot(x, y2, "k-", label='$Theoretical\  Probability$')
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('high_b.pdf', format="pdf")
plt.savefig('high_b.png', format="png")