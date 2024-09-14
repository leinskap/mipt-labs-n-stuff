import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
C = np.array([x*0.01 for x in range(1, 6)])
tau1 = np.array([120, 55, 35.4, 27.6, 22.9])
tau2 = np.array([118, 33.4, 21.9, 16.5, 13.1])
v1 = np.array([1/x for x in tau1])
v2 = np.array([1/x for x in tau2])
fig, ax = plt.subplots(figsize=(6, 7))
ax.set_xlabel('Концетрация, моль$\\cdot л^{-1}$')
ax.set_ylabel('Условная скорость, $c^{-1}$')
# ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.scatter(C, v1, c='black')
ax.scatter(C, v2, c='black')
coefs1 = np.polyfit(C, v1, 1)
coefs2 = np.polyfit(C, v2, 1)
p1 = np.poly1d(coefs1)
p2 = np.poly1d(coefs2)
k1 = coefs1[0]
k2 = coefs2[0]
sigma_k1 = 1 / math.sqrt(4) * math.sqrt(
        abs((st.mean(v1 ** 2) - (st.mean(v1)) ** 2) / (st.mean(C ** 2) - (st.mean(C)) ** 2) - k1 ** 2))
sigma_k2 = 1 / math.sqrt(4) * math.sqrt(
        abs((st.mean(v2 ** 2) - (st.mean(v2)) ** 2) / (st.mean(C ** 2) - (st.mean(C)) ** 2) - k2 ** 2))
ax.plot(C, p1(C), linestyle=':', label="28 $\\degree$C, $k_1$ = " + '(' + str(round(k1, 2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k1, 2)) + ') ' + '$моль \\cdot л^{-1} \\cdot c^{-1}$')
ax.plot(C, p2(C), linestyle=':', label="38 $\\degree$C, $k_2$ = " + '(' + str(round(k2, 2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k2, 2)) + ') ' + '$моль \\cdot л^{-1} \\cdot c^{-1}$')
ax.legend()
sigma = k2/k1 * math.sqrt((sigma_k1/k1)**2 + (sigma_k2/k2)**2)
print(k1, k2, k2/k1, sigma)
print(v1, v2)
plt.savefig('2.png')
T1 = 28 + 273
T2 = 38 + 273
R = 8.314
Ea = math.log(k2/k1) * R * T1 * T2 /(T2 - T1)
print(Ea, Ea * sigma/(k2/k1))
a1 = math.exp(-Ea/(R*T1))
a2 = math.exp(-Ea/(R*T2))
print(a1)
print(a2)
print(k1 / a1)
print(k2 / a2)
fig, ax = plt.subplots()
lnC = [math.log(x) for x in C]
ax.plot(lnC, tau1)
ax.plot(lnC, tau2)

fig, ax = plt.subplots()
lnC = [1/x for x in C]
ax.plot(lnC, tau1)
ax.plot(lnC, tau2)

fig, ax = plt.subplots()
lnC = [1/x**2 for x in C]
ax.plot(lnC, tau1)
ax.plot(lnC, tau2)

plt.show()
