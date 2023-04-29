import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = np.array([0, 0, 0, 0, 0, 0, 0.229918699, 0.068617886, 0.079349593, 0.067317073, 0.021788618, 0.024715447, 0.030569106, 0.030569106, 0.015934959])
y2 = (9.741*(10**(-7))*(x**8))-(0.4*(10**(-4))*(x**7))+(0.8*(10**(-3))*(x**6))-(0.009*(x**5))+(0.062*(x**4))-(0.262*(x**3))+(0.704*(x**2))-(1.142*x)+1
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$P(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y1, "k--", label='$Actual\ Probability$')
plt.plot(x, y2, "k-", label='$Theoretical\  Probability$')
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('high_u.pdf', format="pdf")
plt.savefig('high_u.png', format="png")