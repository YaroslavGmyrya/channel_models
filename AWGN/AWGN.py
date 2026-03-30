import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

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

N = 1000
SNR = 15

# gen bits
bits = np.random.randint(0, 2, N)

# gen symbols
symbols = [complex(i, i) for i in 2*bits-1]

# rx signal
rx = AWGN(symbols, SNR)

plt.subplot(2, 1, 1)
plt.scatter(np.real(symbols), np.imag(symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.grid()
plt.title("Ideal BPSK constellation")

plt.subplot(2, 1, 2)
plt.scatter(np.real(rx), np.imag(rx))
plt.xlabel("I")
plt.ylabel("Q")
plt.grid()
plt.title("Rx BPSK constellation")

plt.show()

# REAL_BER = []
# THEORY_BER = []
# for snr in range(-30, 30, 1):
#     rx = AWGN(symbols, snr)
#     BER = 0
#     rx_bits = [1 if rx[i] > 0 else 0 for i in range(len(rx))]
    
#     for i in range(len(rx_bits)):
#         if rx_bits[i] != bits[i]:
#             BER += 1
#     REAL_BER.append(BER/len(rx_bits))
#     snr_lin = 10**(snr/10)
#     THEORY_BER.append(erfc(np.sqrt(snr_lin)))
    
# plt.plot([i for i in range(-30, 30, 1)], REAL_BER, label="Experemental BER")
# plt.plot([i for i in range(-30, 30, 1)], THEORY_BER, label="Theoretical BER")
# plt.xlabel("SNR_db")
# plt.ylabel("BER")
# plt.title("BER(snr)")
# plt.grid()
# plt.legend()
# plt.show()