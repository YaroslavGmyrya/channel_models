import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.special import j0

models = {
    'TU50': {
        # Typical Urban, 50 km/h
        'delays': np.array([0.0, 0.2, 0.5, 1.6, 2.3, 5.0]) * 1e-6,
        'powers_db': np.array([-3.0, 0.0, -2.0, -6.0, -8.0, -10.0]),
        'velocity_kmh': 50
    },
    'TU3': {
        # Typical Urban, 3 km/h
        'delays': np.array([0.0, 0.2, 0.5, 1.6, 2.3, 5.0]) * 1e-6,
        'powers_db': np.array([-3.0, 0.0, -2.0, -6.0, -8.0, -10.0]),
        'velocity_kmh': 3
    },
    'RA130': {
        # Rural Area, 130 km/h
        'delays': np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5]) * 1e-6,
        'powers_db': np.array([0.0, -4.0, -8.0, -12.0, -16.0, -20.0]),
        'velocity_kmh': 130
    },
    'HT100': {
        # Hilly Terrain, 100 km/h
        'delays': np.array([0.0, 0.1, 0.3, 0.5, 15.0, 17.2]) * 1e-6,
        'powers_db': np.array([0.0, -1.5, -4.5, -7.5, -8.0, -17.7]),
        'velocity_kmh': 100
    },
    'EQ50': {
        # Equalization, 50 km/h
        'delays': np.array([0.0, 3.2, 6.4, 9.6, 12.8, 16.0]) * 1e-6,
        'powers_db': np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        'velocity_kmh': 50
    },
}

def jakes_fading(f_c, v, N, dt, samples_count):
    c = 3e8
    
    # max doppler 
    f_d = (f_c * v) / c

    # signal receiving angle
    alpha = np.random.uniform(0, 2*np.pi, N)
    
    # random phase
    phase = np.random.uniform(0, 2*np.pi, N)

    # samples to time
    t = np.arange(samples_count) * dt
    
    # ray init
    h = np.zeros(len(t), dtype=complex)

    # ray generate
    for i in range(N):
        # current doppler
        f_i = f_d * np.cos(alpha[i])
        
        h += np.exp(1j * (2*np.pi*f_i*t + phase[i]))

    # normalized
    return h / np.sqrt(N)


def COST_207(model_type, f_c, N, dt, samples_count, dd):
    # check model existence
    if model_type not in models:
        print("Invalid area type!")
        sys.exit(1)

    # get model parameters
    model = models[model_type]
    delays = model['delays']
    powers_db = model['powers_db']
    speed = model['velocity_kmh']

    # tap power to linear scale
    lin_power = 10 ** (powers_db / 10)
    
    # delay to samples (dd is delta delay. It is sample duration)
    shifts_on_samples = (delays / dd).astype(int)

    max_shift = np.max(shifts_on_samples) + 1

    # matrix init
    H = np.zeros((samples_count, max_shift), dtype=complex)

    # fill matrix. Cols is a ray
    for power, shift in zip(lin_power, shifts_on_samples):
        H[:, shift] = np.sqrt(power) * jakes_fading(f_c, speed, N, dt, samples_count)

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
fc = 1800e6     # carrier 1800 MHz
dt = 1e-6       # sample duration
dd = 50e-9      # delay duration in samples
N = 128          # sinusoids for one ray

n_bits = 100000

H = COST_207("RA130", fc, N, dt, n_bits, dd)

# rows, cols = H.shape
# t = np.arange(cols) * dd 

# # check avg energy per ray (compare with 'powe_db' in model)

# # avg energy per ray
# E = np.mean(np.abs(H)**2, axis=0)
# E = 10 * np.log10(E + 1e-15)

# plt.stem(t, E)
# plt.xlabel('delay, s')
# plt.ylabel('avg power, dB')
# plt.title('COST207 Profile')
# plt.show()


# check tap PDF

# get first tap
tap = H[:, 0]  

# get amplitude
# amp = np.abs(tap)

# # compute sigma 
# sigma = np.sqrt(np.mean(amp**2) / 2)

# # Emperical
# plt.hist(amp, bins=100, density=True, label="Emperical tap PDF")

# # Theory
# r = np.linspace(0, amp.max(), 500)
# pdf = (r / sigma**2) * np.exp(-r**2 / (2 * sigma**2))

# plt.plot(r, pdf, label="Theory tap PDF")

# plt.title("Amplitude distribution")
# plt.legend()
# plt.show()

# автокорреляция
autocorr = np.correlate(tap, tap, mode="same")

# нормализация (важно!)
autocorr = autocorr / np.max(autocorr)

# ось лагов
lags = np.arange(-len(tap)//2, len(tap)//2)

# теоретическая кривая J0
tau = lags / np.max(lags) * 265
theory = j0(tau)

plt.plot(lags, autocorr, label="Autocorr")
plt.plot(lags, theory, label="J0")
plt.legend()
plt.title("Autocorrelation and Bessel J0")
plt.grid()
plt.show()
# TEST

# generate bits
# bits = np.random.randint(0, 2, n_bits)

# # create BPSK 
# symbols = 2*bits - 1 + 0j

# # channel
# rx_symbols = pass_through_channel(symbols, H)

# # timeline
# t_sig = np.arange(len(symbols)) * dt

# # show signal in output of channel
# plt.plot(t_sig, np.real(rx_symbols), label="Real")
# plt.plot(t_sig, np.imag(rx_symbols), label="Imag")
# plt.legend()
# plt.show()


