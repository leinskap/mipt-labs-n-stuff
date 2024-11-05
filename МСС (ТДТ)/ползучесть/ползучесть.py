import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit


fig, ax = plt.subplots()
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('')
# ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
# plt.savefig('.png')
t = np.array(sorted([0, 0.5, 1, 3, 5, 10, 15, 20, 2, 4, 6, 7]))
l = np.array(sorted([0.5547, 0.7364, 0.7729, 0.8429, 0.8741, 0.9296, 0.9632, 0.9875, 0.8144, 0.8586, 0.8897, 0.9020]))
l0 = 50
S = 5.4 * 19.7 # мм^2
print(S)
F = 61 * 9.8 # H
print(F/S)
print(l/l0)
print((l-l[0])/l0)
P = (l-l[0])/l0 * S / F
x = t
y = P
ax.scatter(x, y)



def func(t, A, B, C, a, b):
    return A-B*np.exp(-a*t) - C * np.exp(-b*t)
popt, pcov = curve_fit(func, x, y, method='trf', maxfev=5000)
print(popt)



ax.plot(np.linspace(0, max(t), 500), func(np.linspace(0, max(t), 500), *popt), label='Аппроксимация')


fig, ax = plt.subplots()
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('')
# ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()


ax.plot(np.linspace(0, max(t), 500), F/S * func(np.linspace(0, max(t), 500), *popt))
ax.scatter(t, (l-l[0])/l0)


plt.show()