import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
# oценка максимальной мощности
k = 25 # мВт/(м*К)
dt = 30
L = 4 # м
r1 = 10 * 10**(-3)
r0 = 0.055 * 10**(-3)
Q_max = 2*math.pi * L * k * dt / 5
I_max = math.sqrt(Q_max/20) * 10
print(I_max)


TList = [23, 30, 50, 60]
I23 = [12.03, 24.08, 36.07, 48.05, 60.02, 72.07, 83.92, 96.03, 108.01]
U23 = [0.245, 0.492, 0.74, 0.992, 1.25, 1.511, 1.78, 2.06, 2.35]

I30 = [12.01, 24.01, 36.04, 48.05, 60.0, 72.04, 83.92, 96.0, 107.99]
U30 = [0.251, 0.503, 0.756, 1.02, 1.28, 1.547, 1.821, 2.107, 2.402]

I50 = [12.06, 24.02, 36.03, 48.04, 59.99, 72.03, 84.05, 95.94, 108.18]
U50 = [0.269, 0.537, 0.809, 1.08, 1.362, 1.649, 1.942, 2.242, 2.56]

I60 = [12.02, 24.0, 36.03, 48.04, 60.08, 72.01, 95.93, 108.18]
U60 = [0.277, 0.554, 0.834, 1.117, 1.407, 1.7, 2.309, 2.637]

data = [(np.array(I23), np.array(U23)), (np.array(I30), np.array(U30)),
        (np.array(I50), np.array(U50)), (np.array(I60), np.array(U60))]
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('Q, Дж')
ax.set_ylabel('$R_{н}$, Ом')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
R0 = []
dRdQ = []
sigma_dRdQ = []
for i in range(4):
    d = data[i]
    T = TList[i]
    Rn = [d[1][j] * 10 ** 3 / d[0][j] for j in range(len(d[0]))]
    Rn = np.array(Rn)

    Q = [d[0][j]*10**(-3)*d[1][j] for j in range(len(d[0]))]
    Q = np.array(Q)

    coefs = np.polyfit(Q, Rn, 1)
    p = np.poly1d(coefs)
    k = coefs[0]
    a = coefs[1]
    sigma_k = 1 / math.sqrt(len(Q)) * math.sqrt(
        (st.mean(Rn ** 2) - (st.mean(Rn)) ** 2) / (st.mean(Q ** 2) - (st.mean(Q)) ** 2) - k ** 2)
    sigma_a = sigma_k * math.sqrt(st.mean(Q**2) - (st.mean(Q))**2)
    dRdQ.append(k)
    sigma_dRdQ.append(sigma_k)
    R0.append(coefs[1])

    print(T+273, ':', round(k, 2), u"\u00B1", round(sigma_k, 2), ',', round(a, 2), u"\u00B1", round(sigma_a, 2))

    ax.scatter(Q, Rn, color='black')
    ax.plot(Q, p(Q), label='T = ' + str(T+273) + ' K; ' + 'k = ' + str(round(k, 2)) + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{Ом}{Дж}$',)
ax.legend()
print('Q', Q)
plt.savefig('Rn(Q).png')



TList = np.array(TList)
R0 = np.array(R0)
TList += 273
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('T, K')
ax.set_ylabel('$R_0$, Ом')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.scatter(TList, R0, c='black')
coefs = np.polyfit(TList, R0, 1)
p = np.poly1d(coefs)
k = coefs[0]
a = coefs[1]
sigma_k = 1 / math.sqrt(4) * math.sqrt(
        abs((st.mean(R0 ** 2) - (st.mean(R0)) ** 2) / (st.mean(TList ** 2) - (st.mean(TList)) ** 2) - k ** 2))
sigma_a = sigma_k * math.sqrt(st.mean(TList**2) - (st.mean(TList))**2)
alpha = k/20
print('dR/dT =', k, u"\u00B1", sigma_k)
print('alpha =', alpha, u"\u00B1", sigma_k/k * alpha)
ax.plot(TList, p(TList), color='0.9', linestyle=':')
kappa = [k * (1 / x) * math.log(r1/r0) / (2 * math.pi * L) for x in dRdQ]
sigma_kappa = [kappa[i] * math.sqrt(0.01**2 + (sigma_k/k)**2 + (sigma_dRdQ[i]/dRdQ[i])**2) for i in range(4)]
for i in range(len(TList)):
    print(TList[i], ':', round(kappa[i]*10000, 2), u"\u00B1", round(sigma_kappa[i], 3))
plt.savefig('R0(T).png')


kappa = np.array(kappa)
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('T, K')
ax.set_ylabel('$\kappa, \\frac{мВт}{м \\cdot K}$')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

coefs = np.polyfit(TList, kappa*10000, 1)
ax.scatter(TList, kappa*10000, c='black')
p = np.poly1d(coefs)
k = coefs[0]
ax.plot(TList, p(TList))
plt.savefig('k(T).png')



fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('$\ln{\\frac{T}{T_0}}$')
ax.set_ylabel('$\ln{\\frac{\\kappa}{\\kappa_0}}$')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
x = [math.log(x) for x in TList/TList[0]]
y = [math.log(x) for x in kappa/kappa[0]]
ax.scatter(x, y, c='black')
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
k = coefs[0]
ax.plot(x, p(x), label='$\\beta$ = ' + str(round(k, 3)))
print('beta = ', coefs[0])
ax.legend()
plt.savefig('lnk(lnT).png')
# plt.show()


print()
# plt.savefig('.png')
