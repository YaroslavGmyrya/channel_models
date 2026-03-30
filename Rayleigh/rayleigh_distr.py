import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


# 1. Theoretical PDF/CDF of Rayleigh distribution

t = np.linspace(0, 5, 1000)
sigma = 1/np.sqrt(2)
mu = 0

theoretical_PDF = (t / sigma**2) * np.exp(-(t**2)/(2*sigma**2))
theoretical_CDF = 1 - np.exp(-(t**2)/(2*sigma**2))

# 2. Emperical PDF/CDF of Rayleigh distribution

N1 = np.random.normal(mu, sigma, len(t))
N2 = np.random.normal(mu, sigma, len(t))

CN = N1 + 1j*N2

R = np.abs(CN)

# 3. Plots

plt.subplot(2, 1, 1)
plt.plot(t, theoretical_PDF, label="theoretical Rayleigh")
plt.hist(R, bins=100, density=True, alpha=0.6, label="empirical Rayleigh")
plt.xlabel("time")
plt.ylabel("R(t)")
plt.title("PDF")
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, theoretical_CDF, label="theoretical Rayleigh")
plt.hist(R, bins=100, density=True, cumulative=True, label="emperical Rayleigh")
plt.xlabel("time")
plt.ylabel("R(t)")
plt.title("CDF")
plt.grid()
plt.legend()
plt.show()
