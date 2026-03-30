import numpy as np
import matplotlib.pyplot as plt
from scipy.special import i0

sigma = 1
mu = 5
A = 1
t = np.linspace(0, 10, 5000)

rice_distr = t/sigma * np.exp(-(t**2 + A**2)/(2*sigma))*i0(t*A/sigma)
rayleigh_distr = t/sigma * np.exp(-(t**2)/(2*sigma))
normal_distr = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(t-mu)**2/(2*sigma))


plt.plot(t, rice_distr, label="Rice PDF")
plt.plot(t, rayleigh_distr, label="Rayleigh PDF")
plt.plot(t, normal_distr, label="Normal PDF")
plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Theoretical PDF")
plt.grid()
plt.legend()
plt.show()