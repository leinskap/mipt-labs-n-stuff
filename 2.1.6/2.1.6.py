import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st


T = np.array([25.2, 33, 37.1, 43])
P1 = np.array([4, 3.6, 2.5, 1.9])
V1 = np.array([0.115, 0.101, 0.060, 0.040])
V1 *= 1000
P1 = P1[::-1]
V1 = V1[::-1]

P2 = np.array([4, 3.5, 3.0, 2.4, 1.8])
V2 = np.array([0.113, 0.094, 0.072, 0.055, 0.036])
V2 *= 1000
P2 = P2[::-1]
V2 = V2[::-1]

P3 = np.array([4, 3.5, 3.0, 2.5, 1.9])
V3 = np.array([0.11, 0.093, 0.072, 0.053, 0.036])
V3 *= 1000
P3 = P3[::-1]
V3 = V3[::-1]

P4 = np.array([4, 3.5, 3.0, 2.4, 1.8])
V4 = np.array([0.113, 0.087, 0.068, 0.048, 0.030])
V4 *= 1000
P4 = P4[::-1]
V4 = V4[::-1]

P = [P1, P2, P3, P4]
V = [V1, V2, V3, V4]

# чувствительность k
k = np.array([40.7, 41.5, 42.4])

mu = []
sigma_mu = []
filename = ['25.png', '33.png', '37.png', '43.png']
for i in range(len(T)):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    # ax.legend()
    plt.grid(True, which='major', color='grey', linestyle='-')
    plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
    plt.minorticks_on()
    # plt.savefig('.png')
    dP = P[i] - P[i][0]
    dV = np.array(V[i] - V[i][0])
    if 20 <= T[i] <= 30:
        dT = 1/k[0]*dV
    elif 30 <= T[i] <= 40:
        dT = 1 / k[1] * dV
    elif 40 <= T[i] <= 50:
        dT = 1 / k[2] * dV
    print(dP, dT, dV)
    ax.scatter(dP, dT, c='black')
    coefs = np.polyfit(dP, dT, 1)
    p = np.poly1d(coefs)
    r = coefs[0]
    sigma_r = 1 / math.sqrt(len(T)) * math.sqrt(
        abs((st.mean(dT ** 2) - (st.mean(dT)) ** 2) / (st.mean(dP ** 2) - (st.mean(dP)) ** 2) - r ** 2))
    ax.plot(dP, p(dP), color='0.9', linestyle=':', label='$\\mu$ = ' + str(round(r, 3)) + ' ' + u"\u00B1" + ' '
                                                   + str(round(sigma_r, 3)) + ' $\\frac{K}{атм}$')
    mu.append(coefs[0])
    sigma_mu.append(sigma_r)
    ax.legend()
    plt.savefig(filename[i])

print(mu)
mu = sorted(mu)
mu = mu[::-1]
mu = np.array(mu)
fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('')
# ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
T1 = [1/(x+273) for x in T]
T1 = np.array(T1) * 1000
ax.scatter(T1, mu, color = 'black')
coefs = np.polyfit(T1, mu, 1)
p = np.poly1d(coefs)
r = coefs[0]
m = coefs[1]

sigma_r = 1 / math.sqrt(len(T)) * math.sqrt(
        abs((st.mean(mu ** 2) - (st.mean(mu)) ** 2) / (st.mean(T1 ** 2) - (st.mean(T1)) ** 2) - r ** 2))
ax.plot(T1, p(T1), color='0.9', linestyle=':')
plt.savefig('mu(1T).png')
a1 = 2*(8.31)**2 * coefs[0]
b1 = 4*8.31  *coefs[1]
sigma_m = sigma_r*math.sqrt((abs(st.mean(T1**2) - (st.mean(T1)) ** 2)))
print(r*1000, sigma_r*1000)
print(m, sigma_m)

a = []
b = []
for i in range(len(T)-1):
    A = 2*8.31**2*(mu[i]-mu[i+1])*(T[i]+273)*(T[i+1]+273)/(T[i+1]-T[i])
    a.append(A)
    B = 4*8.31 * (mu[i+1]*T[i+1] - mu[i]*T[i]) /(T[i]-T[i+1])
    b.append(B)
print(st.mean(a), a1)
print(st.mean(b), b1)
a = st.mean(a)
b = st.mean(b)
print(2*a/(8.31*b), 2*a1*10000/(8.31*b1))
#plt.show()