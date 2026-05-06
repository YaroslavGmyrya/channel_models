import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0
from COST207 import COST_207, models, jakes_fading, pass_through_channel
from itertools import batched


def invert_table(table):
    return {v: k for k, v in table.items()}

def nearest_symbol(symbol, constellation):
    return min(constellation, key=lambda x: abs(symbol - x))

coeff1 = 1/np.sqrt(2)
coeff2 = 1/np.sqrt(10)

BPSK_mod_table = {
    "0": complex(-coeff1, -coeff1),
    "1": complex(coeff1, coeff1),
}

QPSK_mod_table = {
    "00": complex(-coeff1, -coeff1),
    "01": complex(-coeff1,  coeff1),
    "11": complex( coeff1,  coeff1),
    "10": complex( coeff1, -coeff1),
}

QAM16_mod_table = {
    "0000": complex(-3*coeff2, -3*coeff2),
    "0001": complex(-3*coeff2, -1*coeff2),
    "0011": complex(-3*coeff2,  1*coeff2),
    "0010": complex(-3*coeff2,  3*coeff2),

    "0100": complex(-1*coeff2, -3*coeff2),
    "0101": complex(-1*coeff2, -1*coeff2),
    "0111": complex(-1*coeff2,  1*coeff2),
    "0110": complex(-1*coeff2,  3*coeff2),

    "1100": complex( 1*coeff2, -3*coeff2),
    "1101": complex( 1*coeff2, -1*coeff2),
    "1111": complex( 1*coeff2,  1*coeff2),
    "1110": complex( 1*coeff2,  3*coeff2),

    "1000": complex( 3*coeff2, -3*coeff2),
    "1001": complex( 3*coeff2, -1*coeff2),
    "1011": complex( 3*coeff2,  1*coeff2),
    "1010": complex( 3*coeff2,  3*coeff2),
}

def BPSK_mod(bits):
    return [BPSK_mod_table[str(bit)] for bit in bits]

def QPSK_mod(bits):
    blocks = batched(bits, 2)
    return [QPSK_mod_table[''.join(map(str, block))] for block in blocks]

def QAM16_mod(bits):
    blocks = batched(bits, 4)
    return [QAM16_mod_table[''.join(map(str, block))] for block in blocks]

def QAM_mod(mod_type, bits):
    if mod_type == "BPSK":
        return BPSK_mod(bits)
    elif mod_type == "QPSK":
        return QPSK_mod(bits)
    elif mod_type == "QAM16":
        return QAM16_mod(bits)
    

BPSK_demod_table = invert_table(BPSK_mod_table)
QPSK_demod_table = invert_table(QPSK_mod_table)
QAM16_demod_table = invert_table(QAM16_mod_table)

def BPSK_demod(symbols):
    constellation = list(BPSK_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(BPSK_demod_table[nearest])

    return bits

def QPSK_demod(symbols):
    constellation = list(QPSK_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(QPSK_demod_table[nearest])

    return bits

def QAM16_demod(symbols):
    constellation = list(QAM16_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(QAM16_demod_table[nearest])

    return bits

def QAM_demod(mod_type, symbols):
    if mod_type == "BPSK":
        return BPSK_demod(symbols)
    elif mod_type == "QPSK":
        return QPSK_demod(symbols)
    elif mod_type == "QAM16":
        return QAM16_demod(symbols)
    
def AWGN(signal, snr_db):
    signal = np.asarray(signal)

    signal_power = np.mean(np.abs(signal)**2)

    snr_linear = 10**(snr_db / 10)

    noise_power = signal_power / snr_linear

    noise = (
        np.random.normal(0, np.sqrt(noise_power/2), signal.shape) +
        1j*np.random.normal(0, np.sqrt(noise_power/2), signal.shape)
    )

    return signal + noise

def equalize_zf(y, h):
    Y = np.fft.fft(y)
    H = np.fft.fft(h, n=len(y))

    X_hat = Y / H
    x_hat = np.fft.ifft(X_hat)

    return x_hat


TRANNING = np.asarray([0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0])
N_bits = 10
N_sin = 33
SNR = 18
seed = 10

mod_type = "BPSK"
fc = 1800e6     # carrier 1800 MHz
Ts = 1e-9       # sample duration
L = 8

# generate bits
bits = np.random.randint(0, 2, N_bits)
bits = [*TRANNING, *bits]

# generate symbols
symbols = QAM_mod(mod_type, bits)

# COST207 channel
t = np.arange(0, len(symbols), 1) * Ts
H = COST_207("TU3", fc, N_sin, t, Ts)

print(*H)

H_static = H[0, :L]

rx_symbols = np.convolve(symbols, H_static)[:len(symbols)]

# AWGN
rx_symbols = AWGN(rx_symbols, SNR)

plt.scatter(np.real(rx_symbols), np.imag(rx_symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("RX constellation")
plt.grid()
plt.show()

# create tranning matrix
N_t = len(TRANNING)
T = np.zeros((N_t - L + 1, L), dtype=complex)
MOD_TS = QAM_mod(mod_type, TRANNING)

for i in range(L):
    T[:, L-1-i] = MOD_TS[i:i + (N_t - L + 1)]

# extract tranning from 
y = rx_symbols[L-1:N_t]

# estimation
T_H = np.conjugate(T.T)

h_ls = np.linalg.pinv(T) @ y

x_hat = equalize_zf(rx_symbols, h_ls)

delay = L - 1
x_hat = x_hat[delay + len(TRANNING):]

plt.scatter(np.real(x_hat), np.imag(x_hat))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("Recovery constellation")
plt.grid()
plt.show()