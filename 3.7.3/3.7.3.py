import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit










r1 = 1.37/2
r2 = 4/2
c = 2.998*10**8
l = 50.1 # см

# 1. Определение параметров коаксиального кабеля
n = np.linspace(1, 7, 7)

# 50 Ом
R0 = 50

f = np.array([3.88, 7.84, 11.79, 15.73, 19.69, 23.66, 27.64])
# for i in range(len(f)):
#         print(f[i], ' & ', "$", i+1, "\\"+"pi"+"$", ' &   & \\\\')
#         print('\\'+'hline')

fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$\\nu$, кГц')
ax.set_xlabel('n')

ax.scatter(n, f)

coefs = np.polyfit(n, f, 1)
p = np.poly1d(coefs)
k = coefs[0]
x = n
y = f

sigma_k = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(n ** 2) - (st.mean(n)) ** 2) - k ** 2))
ax.plot(x, p(x), label='$\\frac{\\nu}{n}$ = ' + str(round(k,3)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k, 3)) + ' $\\frac{1}{c}$')
ax.legend()
plt.savefig('f(n) 50.png')



vf = k*l
print(vf)
f = np.array([3.88, 7.84, 11.79, 15.73, 19.69, 23.66, 27.64, 31.59, 35.55, 39.5])
n = np.linspace(1, len(f), len(f))
U0 = np.array([54, 54.4, 54.8, 54.8, 54.8, 54, 54, 53.44, 53.27, 52.46])
U = np.array([48.4, 46, 44.4, 43.2, 40, 40.8, 37.6, 37.01, 36.28, 32.9])
k = np.array([2*np.pi*N/l for N in n])
x1 = np.array([2*np.pi*nu**2*1000 for nu in f])
a = np.array([1/l * math.log(U0[i]/U[i]) for i in range(len(U))])


# for i in range(len(f)):
#         print(f[i], ' & ', round(U0[i]/10, 2), ' & ', round(U[i]/10,2), ' & '+"$" +str(2**(i+1))+ "\\"+"pi"+"$", '\\\\')
#         print('\\'+'hline')



y1 = np.array([k[i]**2 - a[i]**2 for i in range(len(k))])


fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('y1, $\\frac{1}{см^2}$')
ax.set_xlabel('x2, $\\frac{рад^2}{c^2}$')

ax.scatter(x1, y1)


x = x1
y = y1
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$\\frac{y1}{x1}$ = ' + str(round(m,7)) + '$\\frac{1}{c}$')
ax.legend()
plt.savefig('y1(x1).png')


LxCx = (2.998*10**10)**2 * m * 10**(-14)
print('LxCx', LxCx)

Lx = c*R0*LxCx**0.5 * 10**9 /c**2
Cx = 1/(R0*c) * LxCx**0.5 * 10**(-9) *c**2
print('Lx', Lx, 'Cx', Cx)

vf = c*100/LxCx**0.5
print(vf)

mu = Lx/(2*math.log(r2/r1))
e = Cx*2*math.log(r2/r1)
print(mu/100,e*100)



# Часть II. Определение удельной проводимости проводников.
# Метод А.


y2 = a
x2 = np.array([g**0.5 for g in f])
fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('y1, $\\frac{1}{см}$')
ax.set_xlabel('x2, $\\frac{1}{\\sqrt{c}}$')

ax.scatter(x2, y2)

x = x2[:4]
y = y2[:4]
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$\\frac{y1}{x1}$ = ' + str(round(m,7)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_m, 7)) + ' $\\frac{1}{c}$')
ax.legend()
sigma = (2*Cx*vf/(c*2*r1*m))**2
print('A',sigma)

plt.savefig('y2(x2).png')
# Метод Б.

y3 = np.array([a[i]*k[i] for i in range(len(k))])
x3 = np.array([g**1.5 for g in f])
fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('y1, $\\frac{1}{см}$')
ax.set_xlabel('x2, $\\frac{1}{\\sqrt{c}}$')

ax.scatter(x3, y3)

x = x3
y = y3
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$\\frac{y1}{x1}$ = ' + str(round(m,6)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_m, 6)) + ' $\\frac{1}{c}$')
ax.legend()
sigma = (4*math.pi*Cx/(c*2*r1*m))**2
print('Б',sigma)
plt.savefig('y3(x3).png')



# Длинная линия. Модель.

f = np.array([1, 5.75, 10.5, 15.25, 20, 29.5, 34.25])
dx = np.array([60-40, 40.8-31, 42.4-32.4, 40.8-33.6, 18-6, 18-5.6, 14.6-3.2])
dphi = dx*10**(-6)*2*math.pi*f*1000
# for i in range(len(f)):
#         print(f[i], ' & ', round(dphi[i],2), '\\\\')
#         print('\\'+'hline')

fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$\\varphi$')
ax.set_xlabel('f')
ax.scatter(f, dphi*20)
ax.plot(np.array([3.88, 7.84, 11.79, 15.73, 19.69, 23.66, 27.64, 31.59, 35.55, 39.5]), k*l, label = 'уравнение 27')
# print(dphi*10000, k*l)
ax.legend()
plt.savefig('phi(f).png')
# plt.show()

# R = 0

f = np.array([3.25, 13.68, 23.28, 30.28, 36.18])

n = np.linspace(1, 10, 10)
U = [2*np.array([2.4, 7.4, 11.6, 16, 19.2, 22, 24, 25, 25.6, 25.8]), 2*np.array([8.8, 22, 22.4, 9.4, 10.8, 22.4, 22.2, 9.8, 13.8, 24.6]), 2*np.array([14.6, 19.4, 8.2, 22.2, 7.2, 22.8, 12, 24.4, 17.8, 28])]
fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
ax.set_ylabel('U')
ax.set_xlabel('n')
plt.minorticks_on()

i=0
for u in U:
        y = u
        x = n
        ax.scatter(x, y, label=str(f[i])+' кГц')
        i+=1
        ax.plot(x, y)
ax.legend()
plt.savefig('weird1.png')




f = np.array([10.5, 20.2, 28.3, 34.7])

n = np.linspace(1, 10, 10)
U = [np.array([20.8, 9.2, 5, 18.2, 25, 22.2, 13.4, 6.2, 17.6, 24.6]), 2*np.array([12.6, 17.2, 21.4, 6.4, 23, 16.4, 19, 24.4, 15.2, 27.6]), 2*np.array([4.8, 19.4, 5.6, 19.2, 16, 14.8, 25.4, 18.8, 28, 36])]

# for i in range(10):
#         print(i+1, ' & ', round(U[0][i]/10,2), ' & ', i+1, ' & ', round(U[1][i]/10,2), ' & ', i+1, ' & ', round(U[2][i]/10,2), ' \\\\')
#         print('\\'+'hline')


fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
ax.set_ylabel('')
ax.set_xlabel('')
plt.minorticks_on()

i=0
for u in U:
        y = u
        x = n
        ax.scatter(x, y, label=str(f[i])+' кГц')
        i+=1
        ax.plot(x, y)
ax.legend()
plt.savefig('weird2.png')


# plt.show()

