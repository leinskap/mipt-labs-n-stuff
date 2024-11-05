import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
k = 24
t0 = 6.9092
T = np.array([14.11, 16.11, 18.11, 20.08, 22.06, 24.06, 26.01, 28, 30, 32, 34.04, 36, 38, 40])
du = -np.array([0.015, 0.0054, 0.0075, 0.0115, 0.0153, 0.017, 0.0202, 0.0215, 0.0227, 0.0232, 0.0202, 0.0197, 0.0187, 0.0178])
dT = -k * np.array([0.015, 0.0054, 0.0075, 0.0115, 0.0153, 0.017, 0.0202, 0.0215, 0.0227, 0.0232, 0.0202, 0.0197, 0.0187, 0.0178])
t = np.array([7.9898, 7.8563, 7.7508, 7.6012, 7.4263, 7.2319, 7.1477, 7.0984, 7.0692, 7.0482, 7.03167, 7.019, 7.0111, 7.0043])
T = T + dT + 273
# print('\\hline')
# for i in range(len(T)):
#         print(round(T[i], 1), ' & ', du[i], ' & ', t[i], '\\\\')
#         print('\\hline')

fig, ax = plt.subplots()



x = T
y = (t**2 - t0**2)

ax.scatter(x, y)

ax.set_xlabel('T, К')
ax.set_ylabel('$\\tau^2 - \\tau_0^2$, $мкс^2$')




plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

plt.savefig('1.png')

fig, ax = plt.subplots()



x = T
y = 1/(t**2 - t0**2)
n=4



coefs = np.polyfit(x[n:], y[n:], 1)
p = np.poly1d(coefs)
m = coefs[0]
ax.scatter(x,y)


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
X = np.linspace(288, max(x), 2)
ax.plot(X, p(X))
print(-coefs[1]/coefs[0])



ax.scatter(x, y)

ax.set_xlabel('T, К')
ax.set_ylabel('$\\frac{1}{\\tau^2 - \\tau_0^2}$, $\\frac{1}{мкс^2}$')





plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()


plt.savefig('2.png')
