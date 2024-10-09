import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit
cm = 1/2.54

a = 2
g = 9.816
b = [np.array([23.5, 23.3, 24, 22.3, 21.6, 23.1, 23]), np.array([23.1, 22.8, 23.4, 22.3, 23.8, 21.8, 22.3]), np.array([22.1, 23.6, 23.1, 22.7, 21.9, 22.1, 23.2])]
f = [np.array([233, 232, 221, 178, 168, 183, 168]), np.array([188, 162, 155, 127, 106, 98, 110]), np.array([183, 178, 144, 110, 102, 99, 111])]
s_b = [f[i]*g/(a*b[i]) for i in range(3)]
s_b = [s/s[0] for s in s_b]
print(s_b)
s_b_mean = [st.mean([s_b[0][i], s_b[1][i], s_b[2][i]]) for i in range(len(s_b[0]))]
print(s_b_mean)

p = np.linspace(0, 90, 7)
p = p*math.pi/180

fig, ax = plt.subplots(figsize=(15.5*cm, 12.5*cm))
ax.scatter(p, s_b_mean, label='Экспериментальные точки')




xdata = np.array(p)
ydata = np.array(s_b_mean)
guess = [0.7, 0.17, 0.0997, 0.021]
def func(x, s0, A, a):
    return s0 + A*np.cos(a*x)
popt, pcov = curve_fit(func, xdata, ydata, method='trf', maxfev=5000)
print('1', popt, np.sqrt(np.diag(pcov)))
x = np.linspace(0, 90, 1000)
x = x*math.pi/180
ax.plot(x, func(x, *popt), label='Аппроксимация')
labels = ['$0$', r'$\frac{\pi}{12}$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$',
          r'$\frac{5\pi}{12}$', r'$\frac{\pi}{2}$']
ax.set_xticklabels(labels)
plt.xticks(np.arange(0, 7*np.pi/12, step=np.pi/12))
ax.set_title('Тригонометрическая функция')
ax.legend()
ax.set_ylabel('$\\frac{\\sigma_{b}(\\varphi)}{\\sigma_{b}(0)}$')
ax.set_xlabel('$\\varphi$, рад')
plt.savefig('тригонометр.png')


fig, ax = plt.subplots(figsize=(15.5*cm, 12.5*cm))
ax.scatter(p, s_b_mean, label='Экспериментальные точки')


def f(x):
    a = 0.64
    b = 1.93
    return a/(a**2 * (np.cos(x))**4 + (np.sin(x))**4 + b*(np.sin(x))**2 * (np.cos(x))**2)**0.5

ax.plot(x, f(x), label='Аппроксимация')
ax.legend()
labels = ['$0$', r'$\frac{\pi}{12}$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$',
          r'$\frac{5\pi}{12}$', r'$\frac{\pi}{2}$']
ax.set_xticklabels(labels)
ax.set_title('Формула (1) по двум точкам')
plt.xticks(np.arange(0, 7*np.pi/12, step=np.pi/12))
ax.set_ylabel('$\\frac{\\sigma_{b}(\\varphi)}{\\sigma_{b}(0)}$')
ax.set_xlabel('$\\varphi$, рад')
plt.savefig('две точки.png')


fig, ax = plt.subplots(figsize=(15.5*cm, 12.5*cm))

xdata = np.array(p)
ydata = np.array(s_b_mean)
def func2(x, a,b):
    return a/(a**2 * (np.cos(x))**4 + (np.sin(x))**4 + b*(np.sin(x))**2 * (np.cos(x))**2)**0.5
popt, pcov = curve_fit(func2, xdata, ydata, method='trf', maxfev=5000)
print('3', np.sqrt(np.diag(pcov)))
x = np.linspace(0, 90, 1000)
x = x*math.pi/180
ax.plot(x, func2(x, *popt), label='Аппроксимация')
ax.scatter(p, s_b_mean, label='Экспериментальные точки')
ax.set_title('Формула (1) программным методом')
ax.set_ylabel('$\\frac{\\sigma_{b}(\\varphi)}{\\sigma_{b}(0)}$')
ax.set_xlabel('$\\varphi$, рад')
print(popt)



labels = ['$0$', r'$\frac{\pi}{12}$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$',
          r'$\frac{5\pi}{12}$', r'$\frac{\pi}{2}$']
ax.set_xticklabels(labels)
plt.xticks(np.arange(0, 7*np.pi/12, step=np.pi/12))
ax.legend()
plt.savefig('пргограм.png')

plt.show()



