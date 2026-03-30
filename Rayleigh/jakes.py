import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, j0
from scipy import signal

f_c = 2e9  # carrier
v = 16.6667 # m/s (60 km/h)
c = 3e8   # speed of light
f_d = (f_c*v) / c # max dopler offset
N = 64  # count of rays

alpha = [k * 2 * np.pi / N for k in range(N)]   # receiving angle

print(f"Carrier frequency: {f_c} Hz")
print(f"Speed: {v} m/s")
print(f"Max dopler frequency offset: {f_d} Hz")
print(f"Count of rays: {N}")
print(f"Receiving angle:\n {alpha}")


t = np.linspace(0, 50, 5000)    # time
h = np.zeros(len(t), dtype=np.complex64)  

for i in range(N):
    f_i = f_d*np.cos(alpha[i])  # dopler offset
    
    phase = np.random.uniform(0, 2*np.pi)   # random phase
    
    h += np.exp(1j*(2*np.pi*f_i*t+phase))   # sum of rays

r = np.abs(h) 

r = r / np.sqrt(np.mean(r**2)) # normalized channel response

x = np.linspace(0, np.max(r), 5000)

pdf_rayleigh = 2 * x * np.exp(-x**2) # theoretical pdf of channel

sq_signal = signal.square(2 * np.pi * 0.8 * t)

rx_signal = sq_signal * r

plt.subplot(5, 1, 1)
plt.plot(t, sq_signal)
plt.title("Signal")
plt.xlabel("time, sec")
plt.ylabel("A, V")
plt.grid()

plt.subplot(5, 1, 2)
plt.plot(t, rx_signal)
plt.title("RX signal")
plt.xlabel("time, sec")
plt.ylabel("A, V")

plt.subplot(5, 1, 3)
plt.hist(np.abs(rx_signal), bins=40, density=True, label="Emperical PDF")
plt.plot(x, pdf_rayleigh, label="Theoretical Rayleigh PDF")
plt.xlabel("X")
plt.ylabel("P(X)")
plt.grid()
plt.legend()
plt.title("RX signal PDF")

# autocorr function 
R = np.correlate(rx_signal, rx_signal, mode="full")
R = R / np.max(R)

plt.subplot(5, 1, 4)
plt.plot(np.arange(-len(R) // 2,len(R) // 2 ), R, label="Emperical autocorr")
plt.plot(np.arange(-len(R) // 2,len(R) // 2 ), j0(np.arange(-len(R) // 2,len(R) // 2 )), label="Theoretical autocorr")
plt.grid()
plt.legend()

x_sorted = np.sort(rx_signal)
cdf = np.arange(1, len(x_sorted)+1) / len(x_sorted)

plt.subplot(5, 1, 5)
plt.plot(x_sorted, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title("CDF of signal")
plt.grid()
plt.show()
