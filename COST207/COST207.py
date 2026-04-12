import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, j0
from scipy import signal
import sys
from dataclasses import dataclass

@dataclass
class Tap:
    delay: float
    power_db: float
    doppler: str


# Typical Urban Taps
Tux = [
    Tap(0.0e-6,  -5.7,  "class"),
    Tap(0.2e-6,  -7.6,  "class"),
    Tap(0.5e-6,  -10.1, "class"),
    Tap(1.6e-6,  -10.2, "class"),
    Tap(2.3e-6,  -10.2, "class"),
    Tap(5.0e-6,  -11.5, "class"),
    Tap(5.2e-6,  -11.8, "class"),
    Tap(6.7e-6,  -13.0, "class"),
    Tap(7.5e-6,  -16.2, "class"),
    Tap(8.2e-6,  -17.3, "class"),
    Tap(10.0e-6, -19.0, "class"),
    Tap(10.8e-6, -19.2, "class"),
    Tap(11.5e-6, -20.3, "class"),
    Tap(13.1e-6, -21.2, "class"),
    Tap(15.3e-6, -22.5, "class"),
    Tap(17.0e-6, -23.8, "class"),
    Tap(18.3e-6, -24.0, "class"),
    Tap(20.0e-6, -25.2, "class"),
    Tap(22.0e-6, -27.8, "class"),
    Tap(24.0e-6, -29.0, "class"),
]

# Rural Taps
Rax = [
    Tap(0.0e-6,    -5.2,  "direct"),
    Tap(0.042e-6,  -6.4,  "class"),
    Tap(0.101e-6,  -8.4,  "class"),
    Tap(0.129e-6,  -9.3,  "class"),
    Tap(0.149e-6, -10.0,  "class"),
    Tap(0.245e-6, -13.1,  "class"),
    Tap(0.312e-6, -15.3,  "class"),
    Tap(0.410e-6, -18.5,  "class"),
    Tap(0.469e-6, -20.4,  "class"),
    Tap(0.528e-6, -22.4,  "class"),
]

# Hilly Terrain  Taps
Htx = [
    Tap(0.0e-6,    -3.6,  "class"),
    Tap(0.356e-6,  -8.9,  "class"),
    Tap(0.441e-6, -10.2,  "class"),
    Tap(0.528e-6, -11.5,  "class"),
    Tap(0.546e-6, -11.8,  "class"),
    Tap(0.609e-6, -12.7,  "class"),
    Tap(0.625e-6, -13.0,  "class"),
    Tap(0.842e-6, -16.2,  "class"),
    Tap(0.916e-6, -17.3,  "class"),
    Tap(0.941e-6, -17.7,  "class"),
    Tap(15.000e-6, -17.6, "class"),
    Tap(16.172e-6, -22.7, "class"),
    Tap(16.492e-6, -24.1, "class"),
    Tap(16.876e-6, -25.8, "class"),
    Tap(16.882e-6, -25.8, "class"),
    Tap(16.978e-6, -26.2, "class"),
    Tap(17.615e-6, -29.0, "class"),
    Tap(17.827e-6, -29.9, "class"),
    Tap(17.849e-6, -30.0, "class"),
    Tap(18.016e-6, -30.7, "class"),
]

allowed_area_type = ["Tux", "Rax", "Htx"]

# Generate Class (Jakes) fading (angle have uniform distribution)
# N - count of sinusoids
# v - speed
# N - count of sinusoids
def jakes_fading(f_c, v, N, dt, samples_count):
    c = 3e8   # speed of light
    f_d = (f_c*v) / c # max dopler offset
    
    alpha = np.random.uniform(0, 2*np.pi, N)
    phase = np.random.uniform(0, 2*np.pi, N)   # random phase

    t = np.arange(samples_count) * dt  # time
    h = np.zeros(len(t), dtype=complex)  

    for i in range(N):
        f_i = f_d*np.cos(alpha[i])  # doppler offset
        h += np.exp(1j*(2*np.pi*f_i*t+phase[i]))   # sum of rays
    
    return h / np.sqrt(N)
    
    
def COST_207(area_type, f_c, v, N, dt, samples_count, dd):
    if area_type not in allowed_area_type:
        print("Invalid area type!")
        sys.exit(1)
        
    lin_power = []
    shifts_on_samples = []
    
    if area_type == "Tux":
        lin_power = [10**(Tux[i].power_db / 10) for i in range(len(Tux))]
        shifts_on_samples = [Tux[i].delay / dd for i in range(len(Tux))]

        
    if area_type == "Rax":
        lin_power = [10**(Rax[i].power_db / 10) for i in range(len(Rax))]
        shifts_on_samples = [Rax[i].delay / dd for i in range(len(Rax))]

        
    if area_type == "Htx":
        lin_power = [10**(Htx[i].power_db / 10) for i in range(len(Htx))]
        shifts_on_samples = [Htx[i].delay / dd for i in range(len(Htx))]
    
    shifts_on_samples = list(map(int, shifts_on_samples))
    max_shift = np.max(shifts_on_samples) + 1
    
    H = np.zeros((samples_count, max_shift)).astype(complex)
    
    for power, shift in zip(lin_power, shifts_on_samples):        
        H[:,shift] = np.sqrt(power) * jakes_fading(f_c, v, N, dt, samples_count)
        
    return H
    
def pass_through_channel(x, H):
    N = len(x)
    L = H.shape[1]
    y = np.zeros(N, dtype=complex)

    for n in range(N):
        for l in range(L):
            if n - l >= 0:
                y[n] += H[n, l] * x[n - l]

    return y

# parameters
fc = 1800e6
dt = 1e-6
dd = 50e-9
v = 13.9
N = 128

# channel matrix
H = COST_207("Tux", fc, v, N, dt, 10000, dd)

# visualization
rows, cols = H.shape
t = np.arange(cols) * dt
pdp = np.mean(np.abs(H)**2, axis=0)
pdp_db = 10 * np.log10(pdp + 1e-15)

plt.stem(t, pdp_db)
plt.xlabel('delay, us')
plt.ylabel('avg power, dB')
plt.title('COST207 Profile')
plt.show()

# TEST

n_bits = 1000

bits = np.random.randint(0, 2, n_bits)
symbols = 2*bits - 1 + 0j
symbols = np.repeat(symbols, 10)

rx_symbols = pass_through_channel(symbols, H)

plt.plot(np.arange(len(symbols))*dt,np.real(rx_symbols))
plt.plot(np.arange(len(symbols))*dt,np.imag(rx_symbols))
plt.show()



