import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import rc
import matplotlib.pyplot as plt
x = np.linspace(-5, 10, 1000)
y1 = (9.741*(10**(-7))*(x**8))-(0.4*(10**(-4))*(x**7))+(0.8*(10**(-3))*(x**6))-(0.009*(x**5))+(0.062*(x**4))-(0.262*(x**3))+(0.704*(x**2))-(1.142*x)+1
plt.clf()  # Ensures a clean plotting canvas.
plt.rc('text', usetex=True)
plt.rc('figure', figsize=(1920, 1080))
plt.rc('font', family='serif', serif=['Computer Modern Roman'], size=14)
plt.ylabel("$P(\delta)$")
plt.xlabel("$\delta$")
plt.plot(x, y1, "k--")
plt.legend(loc='upper right', frameon=False, handlelength=3)
plt.savefig('1.pdf', format="pdf")
plt.savefig('1.png', format="png")