import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit

Ip = np.array([1.31, 1.87, 2.11, 2.73, 3.28, 3.65, 3.84, 4.14, 4.56, 4.81])
Up = np.array([26.56, 26.7, 26.77, 26.95, 27.08, 27.16, 27.18, 27.22, 27.25, 27.27])
#
# for i in range(len(Ip)):
#     print(Up[i], ' & ', Ip[i], '\\\\')
#     print('\\hline')


fig, ax = plt.subplots(figsize=(8,6))
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

x = Ip
y = Up
ax.scatter(x, y)
ax.set_xlabel('$I_р$, мA')
ax.set_ylabel('$U_p$, B')

coefs = np.polyfit(x[1:1+2], y[1:1+2], 1)

p = np.poly1d(coefs)
m = coefs[0]
ax.scatter(x,y)
ax.plot(x, p(x))

R_m = coefs[0]
I_p = np.array([4.71, 3.34, 1.54])
V = [np.array([25.1, 22.02, 19.06, 16.085, 13.01, 10.06, 8.08, 6.09, 4.05, 2.08, 0.51, -31.0, -25.09, -22.09, -19.1, -16.09, -13.03, -10.02, -8.02, -6.01, -4.08, -2.1, -0.5]),
     np.array([-25.029, -22.036, -19.054, -16.058, -13.043, -10.065, -8.027, -6.085, -4.033, -2.05, -0.5, 25.2, 22.083, 19.01, 16.04, 13.1, 11.074, 8.03, 6.016, 4.09, 2.077, 0.69]),
     np.array([25.2, 22.06, 19, 16.094, 13.016, 10.073, 8.101, 6.092, 4.04, 2.071, 0.53, -25.25, -21.28, -19, -16.06, -13.06, -10.09, -8, -6.033, -4.13, -2.08, -0.5])]
I = [np.array([22.53, 21.66, 20.77, 19.85, 18.83, 17.77, 16.9, 15.61, 12.76, 6.93, 0, -27.06, -25.56, -24.7, -23.72, -22.67, -21.57, -20.42, -19.52, -18.59, -16.16, -11.33, -4.91]),
     np.array([-19.42, -18.66, -17.77, -16.97, -16.13, -15.24, -14.39, -13.41, -11.37, -7.6, -3.32, 16.53, 15.94, 15.27, 14.59, 13.88, 13.35, 12.32, 11.13, 8.84, 4.49, 0.45]),
     np.array([9.04, 8.69, 8.3, 7.91, 7.46, 6.97, 6.51, 5.69, 4.21, 2, 0.13, -10.12, -9.67, -9.38, -9, -8.54, -8.03, -7.56, -6.88, -5.7, -3.69, -1.62])]

#
# for i in range(len(V[0])):
#     print(V[0][i], ' & ', I[0][i], ' & ', V[1][i], ' & ', I[1][i], ' & ', V[2][i], ' & ', I[2][i], ' \\\\')
#     print('\\hline')

slopes = []
In = []

for i in range(len(I_p)):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.grid(True, which='major', color='grey', linestyle='-')
    plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
    plt.minorticks_on()
    ax.spines[["left", "bottom"]].set_position(("data", 0))

    ax.spines[["top", "right"]].set_visible(False)



    i1 = min([h for h in I[i] if h>=0])
    i2 = max([h for h in I[i] if h<0])

    di = i2-i1
    c = di/2


    v1 = min([h for h in V[i] if h > 0])
    v2 = max([h for h in V[i] if h <= 0])
    dv = v2 - v1
    d = dv / 2

    coefs = np.polyfit([v2, v1],[i2, i1], 1)

    p = np.poly1d(coefs)
    m = coefs[0]
    ax.set_xlabel('$U$, В', loc='right')
    ax.set_ylabel('$I$, мкА', loc='top')
    # ax.scatter(V[i], I[i])
    # ax.plot([v2,v1], p([v2,v1]))
    y = I[i]-p(0)
    slopes.append(m)
    x = V[i]
    ax.scatter(x, y)

    i1 = min([h for h in y if h >= 0])
    i2 = max([h for h in y if h < 0])



    v1 = min([h for h in x if h > 0])
    v2 = max([h for h in x if h <= 0])

    coefs = np.polyfit([v2, v1], [i2, i1], 1)
    p = np.poly1d(coefs)
    ax.plot([v2,v1], p([v2,v1]))


    coefs1 = np.polyfit(x[0:2], y[0:2], 1)
    p1 = np.poly1d(coefs1)
    ax.plot(x, p1(x))

    coefs2 = np.polyfit(x[11:13], y[11:13], 1)
    p2 = np.poly1d(coefs2)
    ax.plot(x, p2(x))
    In.append((p1(0)+p2(0))/2)

slopes = np.array(slopes)
In = np.array(In)*100
print('In',In)
kT = 1/2 * In/slopes * 1.6 * 10**(-19)
T = kT / (1.38*10**(-23))
# print(T)
# print(kT)




fig, ax = plt.subplots(figsize=(8, 6))
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)

for i in range(len(I_p)):




    i1 = min([h for h in I[i] if h>=0])
    i2 = max([h for h in I[i] if h<0])

    di = i2-i1
    c = di/2


    v1 = min([h for h in V[i] if h > 0])
    v2 = max([h for h in V[i] if h <= 0])
    dv = v2 - v1
    d = dv / 2

    coefs = np.polyfit([v2, v1],[i2, i1], 1)

    p = np.poly1d(coefs)
    m = coefs[0]
    ax.set_xlabel('$U$, В', loc='right')
    ax.set_ylabel('$I$, мкА', loc='top')
    # ax.scatter(V[i], I[i])
    # ax.plot([v2,v1], p([v2,v1]))
    y = I[i]-p(0)
    x = V[i]
    ax.scatter(x, y)

    i1 = min([h for h in y if h >= 0])
    i2 = max([h for h in y if h < 0])



    v1 = min([h for h in x if h > 0])
    v2 = max([h for h in x if h <= 0])

    coefs = np.polyfit([v2, v1], [i2, i1], 1)
    p = np.poly1d(coefs)


    coefs1 = np.polyfit(x[0:2], y[0:2], 1)
    p1 = np.poly1d(coefs1)
    ax.plot(x, p1(x))

    coefs2 = np.polyfit(x[11:13], y[11:13], 1)
    p2 = np.poly1d(coefs2)
    ax.plot(x, p2(x))

S = np.pi*0.2*5.2 * 10**(-6)
mi = 22*1.66 * 10**(-27)
e = 1.6*10**(-19)
me = 9.1 * 10**(-32)
print('kT', kT/1.6 * 10**(19))
print(T)
ne = In*10**(-6)/((0.4*S*e) * np.sqrt(2*1.38*10**(-19)*T/mi))
print('ne',ne)

    

wp = np.sqrt(4*np.pi*ne*e**2/me)
print(wp)

e = 4.8*10**(-10)
ne = ne*10**-6
r_De = np.sqrt(kT/1.6 * 10**(19)/(4*np.pi*ne*e**2))

print('r_de', r_De)

r_D = np.sqrt(1.38*10**(-23)*300/(4*np.pi*ne*e**2))
print('r_d', r_D)

N_D = 4/3 * np.pi * r_D**3 * ne

P = 2*133
n = P/(1.38*10**(-23)*300)

alpha = ne/n

fig, ax = plt.subplots(figsize=(8, 6))
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

ax.scatter(I_p, T)

fig, ax = plt.subplots(figsize=(8, 6))
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

ax.scatter(I_p, ne)

plt.show()





