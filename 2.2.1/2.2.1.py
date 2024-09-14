import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import statistics as st
V = 800 * 10**(-6)
sigma_V = 5 * 10**(-6)
LS = 15 * 100
sigma_LS = 0.1 * 100
sigma_D = []
fig, ax = plt.subplots(figsize=(8,5))
D = []
i = 0
filenames = ['41.2.csv', '71.3.csv', '100.5.csv', '131.3.csv', '161.3.csv', '191.3.csv']
pr = np.array([41.2, 71.3, 100.5, 131.3, 161.3, 191.3])
for filename in filenames:
    data = np.loadtxt(filename, skiprows=1, delimiter=',')
    U = [math.log(y) for y in data[:, 1]]
    y = np.array([x/math.log(data[0, 1]) for x in U])
    x = np.array(data[:, 0])
    ax.plot(x, y, label=str(pr[i]))

    coefs = np.polyfit(x, y, 1)
    p = np.poly1d(coefs)
    # ax.plot(-1/coefs[0] * x + coefs[1], linestyle='--')
    k = coefs[0]
    sigma_k = 1/math.sqrt(len(data)) * math.sqrt( (st.mean(y**2) - st.mean(y)**2) / (st.mean(x**2) - st.mean(x)**2) - k**2)
    epsilon_k = -sigma_k/k
    # print(k, epsilon_k)
    D.append(-0.5*k*V*LS * 10**4)
    sigma_D.append(-0.5*k*V*LS * 10**4 * math.sqrt((epsilon_k)**2 + (5/800)**2 + (0.1/15)**2))
    i += 1
print(D)
print(sigma_D)
ax.set_xlabel('t, с')
ax.set_ylabel('$\ln \\frac{U}{U_0}$')
ax.legend()
# fig.savefig('U(t).png')

plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

y = np.array(D)
x = np.array([1/(t) for t in pr])

ax.scatter(x, y)
ax.set_xlabel('$\\frac{1}{P}$, 1/торр')
ax.set_ylabel('D, см^2/c')
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1/math.sqrt(len(D)) * math.sqrt( (st.mean(y**2) - st.mean(y)**2) / (st.mean(x**2) - st.mean(x)**2) - k**2)
D0 = p(1/760)
sigma_D0 = D0 * math.sqrt((sigma_k/k)**2)
print(D0, u"\u00B1", sigma_D0, 'см^2/c')

ax.plot(x, p(x))
Lambda = 3 * D0 * 10**(-4) * math.sqrt(math.pi * 4*10**(-3)/(8*8.314*273.2))
sigma_lambda = Lambda * math.sqrt((sigma_D0/D0)**2)
print(Lambda * 10**9, u"\u00B1", sigma_lambda * 10**9, 'нм')
sigma = 1.38 * 10**(-23) * 273.2 / (760*133.322 * Lambda)
sigma_sigma = sigma * math.sqrt(0.01**2 + (sigma_lambda/Lambda)**2)
print(sigma * 10**(19), u"\u00B1", sigma_sigma * 10**(19), 'e-19', 'м^2')
# fig.savefig('D(1/p).png')


