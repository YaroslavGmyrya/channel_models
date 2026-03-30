import numpy as np
import matplotlib.pyplot as plt

# parameters
sigma = 5
m = 0
N = 10000
Fs = 1e4

# generate normal noise
n = np.random.normal(m, sigma, N)

# calculate PSD - Power Spectrum Density (power on frequency)
X = np.fft.fft(n)
PSD = (1 / N) * np.abs(X) ** 2
PSD = np.fft.fftshift(PSD)
freqs = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))

# calculate autocorr

R = np.correlate(n, n, mode='full') / N

# build plots
plt.subplot(221)
plt.plot(n)
plt.xlabel("sample")
plt.ylabel("value")
plt.title("Normal noise")

plt.subplot(222)
plt.plot(freqs, np.abs(PSD))
plt.xlabel("frequency, Hz")
plt.ylabel("|N(f)|")
plt.title("PSD")

plt.subplot(223)
plt.plot([i for i in range(-N, N-1, 1)],R)
plt.xlabel("lag")
plt.ylabel("value")
plt.title("Autocorr function")

plt.subplot(224)
plt.hist(n, 200)
plt.xlabel("value")
plt.ylabel("density")
plt.title("Density distr")

plt.show()