import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0
from COST207 import COST_207, models, jakes_fading



# parameters
fc = 1800e6     # carrier 1800 MHz
Ts = 1e-6
n_samples = 100000
seed = 10

t = np.arange(0, n_samples, 1) * Ts

mse = []

f_d = (fc*50) / 3e8
N_total = np.arange(33, 34, 1)
realizations = 1

for N in N_total:
    tmp = 0
    for i in range(realizations):
        seed = 10+i
        # get first row (ray)
        ray = jakes_fading(f_d, N, t, seed)

        # compute autocorrelation function (emperical)
        emp_corr = np.correlate(ray, ray, mode="full")
        emp_corr /= np.max(emp_corr)

        tau = np.arange(-len(emp_corr)//2, len(emp_corr)//2)*Ts

        # compute theoretical autocorr function
        # sigma = np.sqrt(np.mean(ray**2)/2)

        th_corr = j0(2*np.pi*f_d*tau)


        print(N)
        plt.plot(tau, emp_corr, label="emperical")
        plt.plot(tau, th_corr, label="theoretical")
        plt.grid()
        plt.legend()
        plt.xlabel("t, s")
        plt.ylabel("R(t)")
        plt.title("Autocorrelation function of Jakes ray")
        plt.show()

        tmp += np.mean(np.abs(th_corr - emp_corr)**2)

    # compute MSE
    mse.append(tmp/realizations)

plt.plot(N_total, mse)
plt.grid()
plt.xlabel("N")
plt.ylabel("MSE(N)")
plt.title("MSE")
plt.show()

index = np.argmin(mse)

print(f"BEST N: {index} \t ERROR: {mse[index]}",)

