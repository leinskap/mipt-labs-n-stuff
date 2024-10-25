import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit




# Обратоботка результатов
# 1

RL = np.array([28.8, 29.2, 30.8, 43, 86])
print('RL')
for c in RL:
    print(c, end=" & ")
print('\n')

L = np.array([100, 99.98, 99.97, 100.6, 103])
print('L')
for c in L:
    print(c, end=" & ")
print('\n')

nu = np.array([50, 500, 1500, 5000, 10000])
print('nu')
for c in nu:
    print(c, end=" & ")
print('\n')

fig, ax = plt.subplots()
ax.scatter(nu, L)
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$L$, мГн')
ax.set_xlabel('$\\nu$, Гц')
# ax.set_title('График $L = L(\\nu) $')

coefs = np.polyfit(nu, L, 2)
l = np.poly1d(coefs)
x = np.linspace(min(nu), max(nu), 50)
ax.plot(x, l(x))

plt.savefig('индуктивность.png')




fig, ax = plt.subplots()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$R_{L}$, Ом')
ax.set_xlabel('$\\nu$, Гц')
# ax.set_title('График $R_{L} = R_{L}(\\nu) $')
ax.scatter(nu, RL)

coefs1 = np.polyfit(nu, RL, 2)
p1 = np.poly1d(coefs1)
x = np.linspace(min(nu), max(nu), 50)
ax.plot(x, p1(x))

plt.savefig('активсопр.png')










L = 100 # мГн
C0 = 1.1
C = np.linspace(1,9,9) # нФ
# print('C')
# for c in C:
#     print(c, end=" & ")
# print('\n')
nu = np.array([10.87, 9.04, 7.80, 7.04, 6.44, 5.94, 5.58, 5.25, 5.02])
print('nu')
for c in nu:
    print(c, end=" & ")
print('\n')

T = 1/(nu) *1000
T_teor = [2*math.pi*(l(nu[i])*(C[i]+C0))**0.5 for i in range(len(C))]
epsilon_T = 0.2/66.4

T0 = 66.4 * 10**(-6) # с
C0 = 1/(4*L*math.pi**2*T0**2)

fig, ax = plt.subplots()
ax.scatter(T_teor, T)
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$T_{эксп}$, мкс')
ax.set_xlabel('$T_{теор}$, мкс')

coefs = np.polyfit(T_teor, T, 1)
p = np.poly1d(coefs)
ax.plot(T_teor, p(T_teor), label = 'Коэффициент наклона '+str(round(coefs[0], 3)))
ax.legend()
k = coefs[0]
T = np.array(T)
T_teor = np.array(T_teor)
sigma_k = 1 / math.sqrt(len(C)) * math.sqrt(
        abs((st.mean(T ** 2) - (st.mean(T)) ** 2) / (st.mean(T_teor ** 2) - (st.mean(T_teor)) ** 2) - k ** 2))
print(sigma_k)
plt.savefig('периоды.png')





# 2

R = np.array([420, 574, 820, 1230, 1640, 2050])
print('R')
for c in R:
    print(c, end=" & ")
print('\n')
theta = np.array([1/4 * math.log(680/88), 1/3 * math.log(644/124), 1/3 * math.log(628/68), 1/2 * math.log(584/56), 1/2 * math.log(556/28), 1/1 * math.log(516/84)])
print('theta')
for c in theta:
    print(round(c, 2), end=" & ")
print('\n')
R_sum = R + p1(5020)

print('R_sum')
for c in R_sum:
    print(round(c), end=" & ")
print('\n')


y = 1/theta**2
x = 1/R_sum**2


fig, ax = plt.subplots()

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$\\frac{1}{\\theta^2}$')
ax.set_xlabel('$\\frac{1}{R_{\Sigma}^2} \\text{ } \\frac{1}{Ом^2}$ ')

ax.scatter(x, y)

coefs = np.polyfit(x[-2:], y[-2:], 1)
p = np.poly1d(coefs)
ax.plot(x, p(x), label = 'Коэффициент наклона '+ str(round(coefs[0]*10**(-6), 3)))

R_cr = 2*math.pi*(coefs[0])**0.5

print(R_cr)

ax.legend()

plt.savefig('декременты.png')




# 3

R_cr_theor = 8.2

# 4

Q_min = math.pi/max(theta[:-1])
Q_max = math.pi/min(theta)
print(Q_max, Q_min)

# 5
theta_spiral = np.array([1/3 * math.log(3.2), 1/2 * math.log(31/11), 1/1 * math.log(31/12), 1/1 * math.log(3), 1/1 * math.log(34/3), 1/1 * math.log(23/2)])
print('theta spiral')
for c in theta_spiral:
    print(round(c,2), end=" & ")
print('\n')
Q_max_spiral = math.pi/min(theta_spiral)
Q_min_spiral = math.pi/max(theta_spiral[:-1])
print(Q_max_spiral, Q_min_spiral)

# 6
C = 6 * 10**(-9)
L = 100 * 10**(-3)
Q_theor = 1/R_sum[:-1] * (L/C)**0.5
print('Q theor',max(Q_theor), min(Q_theor))

# 7
R = [420, 1640]
U0 = [8, 2.5]
nu0 = [5970, 6100]
U = [np.array([3.2, 3.6, 4, 4.4, 5, 5.4, 6.1, 6.8, 7.4, 7.7, 8, 7.6, 6.9, 6.2, 5.3, 4.8, 4.2, 3.9, 3.6, 3.4, 3.2]), np.array([0.96, 1.02, 1.18, 1.26, 1.36, 1.48, 1.64, 1.72, 1.84, 2.21, 2.5, 2.1, 1.72, 1.52, 1.24, 1.1, 1.08, 1.08, 1.06, 1.04, 1])]
nu = [np.array([5310, 5376, 5442, 5508, 5574, 5640, 5706, 5772, 5838, 5904, 5970, 6085, 6200, 6315, 6430, 6545, 6660, 6775, 6890, 7005, 7120]), np.array([4200, 4300, 4500, 4600, 4700, 4800, 5000, 5100, 5200, 5500, 6100, 7360, 8630, 9890, 13690, 18750, 21280, 23810, 26340, 28870, 31400])]

for i in range(len(U[0])):
    print(U[0][i], ' & ', nu[0][i], ' & ', U[1][i], ' & ', nu[1][i], "\\\\")
    print('\\hline')

fig, ax = plt.subplots()

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_ylabel('$\\frac{U}{U_{0}}$')
ax.set_xlabel('$\\frac{\\nu}{\\nu_{0}}$')


ax.scatter(nu[0]/nu0[0], U[0]/U0[0], label = 'R = 420 Ом')
# ax.scatter(nu[1][:-7]/nu0[1], U[1][:-7]/U0[1], label = 'R = 1640 Ом')
ax.axhline(y = 1/2**0.2, linestyle='-.', label='$\\frac{U}{\\sqrt{U_{0}}} = \\frac{1}{\\sqrt{2}}$')

coefs = np.polyfit(nu[0]/nu0[0], U[0]/U0[0], 6)
p = np.poly1d(coefs)
xdat = np.linspace(0.9, 1.12, 100)
ax.plot(xdat, p(xdat))

x = nu[1]/nu0[1]
y = U[1]/U0[1]
n=13
x=x[:n]
y=y[:n]
xdat = np.linspace(0.7, 1.15, 100)
coefs = np.polyfit(x, y, 6)
p = np.poly1d(coefs)
ax.plot(xdat, p(xdat))

ax.legend()
plt.savefig('ачх.png')

delta_omega = 1.041-0.9695
Q_420 = 1/delta_omega/2
delta_omega = 1.133-0.90
Q_1640 = 1/delta_omega/2
print(Q_420, Q_1640)




R = [100, 800]
f = np.array([6407, 6440, 6473, 6506, 6539, 6605, 6638, 6671, 6704, 6737, 6803, 6836, 6869, 6902, 6935, 6968, 7001, 7034, 7067, 7100])
f = 2*math.pi*f
x = [68.4,  67.2, 65.6, 64, 61.6, 56.4, 53.6, 49.2, 44.4, 40, 30, 24, 19.6, 17.2, 14.4, 12.8, 11.6, 10, 8.8, 7.6]
omega = f*2*math.pi
phase = [omega[i]*x[i]*10**(-6) for i in range(len(x))]
phase = phase/max(phase) * np.pi
df = [[6407, 6440, 6473, 6506, 6539, 6605, 6638, 6671, 6704, 6737, 6803, 6836, 6869, 6902, 6935, 6968, 7001, 7034, 7067, 7100], [3161, 3572, 3983, 4394, 4805, 5216, 5627, 6038, 6449, 6860, 7271, 7680, 8090, 8504, 8920, 9330, 9740, 10150, 10559]]
dx = [[68.4,  67.2, 65.6, 64, 61.6, 56.4, 53.6, 49.2, 44.4, 40, 30, 24, 19.6, 17.2, 14.4, 12.8, 11.6, 10, 8.8, 7.6], [130, 116, 104, 93.6, 84.4, 74.4, 65, 55.8, 43.2, 28, 17.2, 10.6, 7.6, 5.4, 3.4, 2.8, 2.4, 1.6, 1.8]]
# for i in range(len(dx[0])):
#     print(dx[0][i], ' & ', df[0][i], ' & ', dx[1][i], ' & ', df[1][i], "\\\\")
#     print('\\hline')




fig, ax = plt.subplots()

# y_pi   = y/np.pi
# unit   = 0.25
# y_tick = np.arange(-0.5, 0.5+unit, unit)
#
# y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
# ax.set_yticks(y_tick*np.pi)
# ax.set_yticklabels(y_label)

ax.scatter(omega, phase)
CR = 6*10**(-9) * R[0]


coefs = np.polyfit(omega, phase, 6)
p = np.poly1d(coefs)

x = np.linspace(min(omega), max(omega), 500)
ax.axhline(y = np.pi/2, linestyle='-.', label='$\\frac{\pi}{2}$')

ax.plot(x, p(x))


omega0 = 267830

o = np.linspace(min(omega), omega0, 500)
ax.plot(o, np.pi-p(o), linestyle = '--')
ax.axhline(y = np.pi/4, linestyle='-.', label='$\\frac{\pi}{4}$', color='tab:orange')

Q_pf = omega0/(-263230+272990)
print('100', Q_pf/5)

ax.legend()
ax.set_ylabel('$\\varphi$, рад')
ax.set_xlabel('$\omega$, рад/с')
plt.savefig('фчх1.png')





f = np.array([3161, 3572, 3983, 4394, 4805, 5216, 5627, 6038, 6449, 6860, 7271, 7680, 8090, 8504, 8920, 9330, 9740, 10150, 10559])
f = 2*math.pi*f
x = [130, 116, 104, 93.6, 84.4, 74.4, 65, 55.8, 43.2, 28, 17.2, 10.6, 7.6, 5.4, 3.4, 2.8, 2.4, 1.6, 1.8]
omega = f*2*math.pi
phase = [omega[i]*x[i]*10**(-6) for i in range(len(x))]
phase = phase/max(phase) * np.pi






fig, ax = plt.subplots()

# y_pi   = y/np.pi
# unit   = 0.25
# y_tick = np.arange(-0.5, 0.5+unit, unit)
#
# y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
# ax.set_yticks(y_tick*np.pi)
# ax.set_yticklabels(y_label)

ax.scatter(omega, phase)
CR = 6*10**(-9) * R[0]


coefs = np.polyfit(omega[:-2], phase[:-2], 6)
p = np.poly1d(coefs)

x = np.linspace(min(omega), max(omega[:-2]), 500)
ax.axhline(y = np.pi/2, linestyle='-.', label='$\\frac{\pi}{2}$')

ax.plot(x, p(x))


omega0 = 269900

o = np.linspace(min(omega), omega0, 500)
ax.plot(o, np.pi-p(o), linestyle = '--')
ax.axhline(y = np.pi/4, linestyle='-.', label='$\\frac{\pi}{4}$', color='tab:orange')

Q_pf = omega0/(-241300+297800)
print('800 ', Q_pf/2)
ax.legend()
ax.set_ylabel('$\\varphi$, рад')
ax.set_xlabel('$\omega$, рад/с')
plt.savefig('фчх2.png')




# 11
U0 = 1.56
# 420 Ом
# Нарастание
theta = 1/4 * math.log((U0-0.89)/(U0-1.44))
print('1up', math.pi/theta)

# Затухание
theta = 1/4 * math.log(1.03/0.22)
print('1down',math.pi/theta)


# 1640 Ом
# Нарастание
theta = 1/2 * math.log((U0-0.15)/(U0-0.48))
print('2up',math.pi/theta/10)

# Затухание
theta = 1/2 * math.log(450/40)
print('2down',math.pi/theta)






























