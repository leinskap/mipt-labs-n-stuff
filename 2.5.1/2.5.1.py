import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st

h1 = 25
h2 = 8
sigma_P = 0.1 * 9.80665
r = 2*22.78*10**(-3)/(49*0.2*9.80665)
sigma_r = r * sigma_P/(49*0.2*9.80665)

T = np.array([24, 30.4, 35.4, 40.4, 45.4, 50.4, 55.3, 59.9])
T += 273
P = np.array([233, 229, 227, 225, 224, 223, 222, 219])
P -= 83
P = P * (0.2 * 9.80665)

sigma_T = 0.5
print(r, sigma_r, P, '\n')
sigma = np.array([r*p/2 for p in P])
sigma_sigma = np.array([sigma[i] * math.sqrt((sigma_P/P[i])**2 + (sigma_r/r)**2) for i in range(len(P))])
print(sigma*1000, '\n')
print(sigma_sigma, '\n')
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('Т, К')
ax.set_ylabel('$\\sigma$, $\\frac{Н}{м}$')


plt.minorticks_on()
ax.scatter(T, sigma, c='black')
coefs = np.polyfit(T, sigma, 1)
p = np.poly1d(coefs)

k = coefs[0]
sigma_k = 1 / math.sqrt(len(T)) * math.sqrt(
        abs((st.mean(sigma ** 2) - (st.mean(sigma)) ** 2) / (st.mean(T ** 2) - (st.mean(T)) ** 2) - k ** 2))
print('dsigma/dT =', k*1000, sigma_k*1000, '\n')
ax.plot(T, p(T), color='0.9', linestyle=':', label='k = ' + str(round(k*1000, 2)) + ' ' + u"\u00B1" + ' '
                                                   + str(round(sigma_k*1000, 2)) + ' $\\frac{мН}{м \\cdot K}$')
ax.legend()
plt.savefig('sigma(T).png')
# ---------------------------------------------------------------------------------------------------------------------

q = np.array([-t*k for t in T])
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('T, K')
ax.set_ylabel('q, $\\frac{Дж}{м^2}$')
ax.set_title('')
print("Tk:")
Tk = [T[i]/2*math.exp(sigma[i]/q[i]) for i in range(len(T))]
print(Tk)
print(st.mean(Tk))
plt.minorticks_on()
ax.scatter(T, q, c='black')
coefs = np.polyfit(T, q, 1)
p = np.poly1d(coefs)
ax.plot(T, p(T), color='0.9', linestyle=':')
plt.savefig('q(T).png')



# ---------------------------------------------------------------------------------------------------------------------
u = np.array([sigma[i] + T[i]*abs(k) for i in range(len(T))])
print(T)
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('T, K')
ax.set_ylabel('$\\frac{U}{F}$, $\\frac{Дж}{м^2}$')

plt.minorticks_on()
ax.scatter(T, u, c='black')
ax.set_ylim([0.11, 0.12])
coefs = np.polyfit(T, u, 1)
p = np.poly1d(coefs)
ax.plot(T, p(T), color='0.9', linestyle=':')
plt.savefig('u(T).png')

plt.show()

# plt.savefig('.png')
