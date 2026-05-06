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

def jakes_fading(f_d, N, t, seed=10):
    np.random.seed(seed)

    phi = np.random.uniform(0, 2*np.pi)     
    theta = np.random.uniform(0, 2*np.pi)    

    phase = np.random.uniform(0, 2*np.pi, N) 

    Xr = np.zeros(len(t))
    Xi = np.zeros(len(t))

    # ray generate
    for i in range(N):

        alpha = (2*np.pi*(i+1) - np.pi + theta) / (4*N)

        Xr += np.sqrt(2/N) * np.cos(phase[i]) * np.cos(2*np.pi*f_d*t*np.cos(alpha) + phi)

        Xi += np.sqrt(2/N) * np.sin(phase[i]) * np.cos(2*np.pi*f_d*t*np.cos(alpha) + phi)

    h = Xr + 1j*Xi

    return h


def COST_207(model_type, f_c, N, t, dd):
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
    H = np.zeros((len(t), max_shift), dtype=complex)

    c = 3e8
    f_d = (f_c * speed) / c

    # fill matrix. Cols is a ray
    for power, shift in zip(lin_power, shifts_on_samples):
        H[:, shift] = np.sqrt(power) * jakes_fading(f_d, N, t)

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

