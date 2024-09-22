import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import curve_fit
import xarray as xr
from matplotlib.ticker import FormatStrFormatter

K = 3.5*10**(-2)
sigma_K = 10**(-4)
ra = 12
sigma_ra = 0.1
Va = [70, 80, 100, 120, 110]
Ia = [np.array([0, 0, 1, 2, 3, 4, 5, 7, 10, 15, 21, 30, 37, 37]), np.array([0, 0, 1, 2, 3, 4, 5, 10, 15, 21, 30, 38, 38]), np.array([0, 0, 1, 2, 3, 4, 5, 10, 15, 20, 38, 38, 38]), np.array([0, 0, 1, 2, 3, 4, 5, 10, 15, 20, 30, 38, 38]), np.array([0, 0, 1, 2, 3, 4, 5, 10, 15, 20, 29, 37, 37])]
Ic = [np.array([15, 8, 7.3, 7, 7, 6.5, 6.5, 6.4, 6, 6, 6.1, 6.2, 3, 0]), np.array([20, 9, 8, 7.6, 7.5, 7.2, 7.1, 7, 6.9, 6.8, 6.7, 6.9, 0]), np.array([35, 20, 19.2, 17, 16.5, 16, 15.9, 15.2, 15, 15, 6.5, 5, 0]), np.array([33, 21, 20.5, 19, 18.5, 18, 17.9, 17.1, 17, 16, 16.5, 4, 0]), np.array([70, 50, 49, 45, 44, 42.5, 42, 40.5, 40.1, 40, 38.5, 15, 0])]
k_I = [1.5, 1.5, 0.75, 0.75, 0.3]
Ia_max = 155
Ic_max = 75
B = [Ic[i]*k_I[i]/Ic_max*K*1000 for i in range(5)]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
markers = ['<', 'o', 'p', 's', 'h']
B_cr = []
fig, ax = plt.subplots(figsize=(8, 5))
for i in range(len(Va)):
    j = Ia[i]*1.5/Ia_max
    ax.scatter(B[i], j, label='$U_a$ = '+str(Va[i]) + ' B', marker=markers[i], color=colors[i])
    a = st.mean(B[i][-6:-4])
    B_cr.append(a)
    ax.axvline(x=a, label='$B_{кр}$ = '+str(round(a, 1)) + ' мТл', color=colors[i])
ax.legend()
ax.set_xlabel('B, мТл')
ax.set_ylabel('I, А')

plt.savefig('Bкр.jpg')

B_cr = np.array(B_cr)
Va = np.array(Va)

fig, ax = plt.subplots(figsize=(8, 5))
B_cr2 = B_cr**2
ax.scatter(Va, B_cr2)
coefs = np.polyfit(Va, B_cr2, 1)
p = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1 / math.sqrt(len(Va)) * math.sqrt(
        abs((st.mean(B_cr2 ** 2) - (st.mean(B_cr2)) ** 2) / (st.mean(Va ** 2) - (st.mean(Va)) ** 2) - k ** 2))
ax.plot(Va, p(Va), label='$\\frac{B_{кр}^2}{U_a}$ = ' + str(round(k,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{мТл^2}{В}$')
ax.set_ylabel('$B_{кр}^2$, $мТл^2$')
ax.set_xlabel('$U_a$')

e_to_m = [8*Va[i]/(B_cr2[i]*10**(-6)*ra**2*10**(-6)) for i in range(len(Va))]
e_to_m = np.array(e_to_m)
e_to_m_mean = st.mean(e_to_m)
sigma_mean = math.sqrt(1/20 * sum((e_to_m-e_to_m_mean)**2))
print(e_to_m_mean*10**(-11), sigma_mean*10**(-11))


ax.legend()
plt.savefig('Bкр2.jpg')



F_max1 = 100
F_max2 = 10
I = np.array([0.47, 0.14, 0.07, 0.21, 0.28, 0.37])
F_K1 = np.array([5-4.2, 4.8-4.6, 4.3-4.1, 4.3-4, 4.5-4.1, 4.4-3.8])
F_K1 = F_K1*F_max2/F_max1

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(I, F_K1)
coefs = np.polyfit(I, F_K1, 1)
p1 = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1 / math.sqrt(len(I)) * math.sqrt(
        abs((st.mean(F_K1 ** 2) - (st.mean(F_K1)) ** 2) / (st.mean(I ** 2) - (st.mean(I)) ** 2) - k ** 2))
ax.plot(I, p1(I), label='$\\frac{\Phi}{I}$ = ' + str(round(k,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{мВб}{А}$')
ax.legend()
ax.set_xlabel('I, A')
ax.set_ylabel('$\Phi$, мВб')
plt.savefig('phi1.jpg')

F_K2 = np.array([4.2-3.6, 4.5-4.3, 4.1-4, 3.9-3.7, 4.1-3.7, 3.8-3.3])
F_K2 = F_K2*F_max2/F_max1



fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(I, F_K2)
coefs = np.polyfit(I, F_K2, 1)
p2 = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1 / math.sqrt(len(I)) * math.sqrt(
        abs((st.mean(F_K2 ** 2) - (st.mean(F_K2)) ** 2) / (st.mean(I ** 2) - (st.mean(I)) ** 2) - k ** 2))
ax.plot(I, p2(I), label='$\\frac{\Phi}{I}$ = ' + str(round(k,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{мВб}{А}$')
ax.legend()
ax.set_xlabel('I, A')
ax.set_ylabel('$\Phi$, мВб')
plt.savefig('phi2.jpg')



V = 0.86*1000
l = 0.265
SN = 0.3
n = [1, 2, 3, 4, 5]
n = np.array(n)
I1 = [0.56, 1.17, 1.74, 2.34, 3.19]
I2 = [0.57, 1.15, 1.76, 2.88, 3.27]
B1 = np.array([p1(I1[i])/SN * 10**(-3) for i in range(len(I1))])
B2 = np.array([p2(I2[i])/SN * 10**(-3) for i in range(len(I2))])

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(n, B1*1000)

ax.set_xlabel('n')
ax.set_ylabel('B, мВб')

coefs = np.polyfit(n, B1*1000, 1)
p = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1 / math.sqrt(len(n)) * math.sqrt(
        abs((st.mean(B1*1000 ** 2) - (st.mean(B1*1000)) ** 2) / (st.mean(n ** 2) - (st.mean(n)) ** 2) - k ** 2))
ax.plot(n, p(n), label='$\\frac{B}{n}$ = ' + str(round(k,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k/1000, 2)) + ' мВб')
ax.legend()
e_to_mA = 8*math.pi**2 * V/l**2 /(k/1000)**2
sigma_e_to_mA = e_to_mA * math.sqrt(2) *sigma_k

#ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
plt.xticks(n)
plt.savefig('Bn1.jpg')

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(n, B2*1000)

ax.set_xlabel('n')

coefs = np.polyfit(n, B2*1000, 1)
p = np.poly1d(coefs)
k = coefs[0]
sigma_k = 1 / math.sqrt(len(n)) * math.sqrt(
        abs((st.mean(B2*1000 ** 2) - (st.mean(B2*1000)) ** 2) / (st.mean(n ** 2) - (st.mean(n)) ** 2) - k ** 2))
ax.plot(n, p(n), label='$\\frac{B}{n}$ = ' + str(round(k,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_k/1000, 2)) + ' мВб')
ax.legend()

plt.xticks(n)
ax.set_ylabel('B, мВб')
plt.savefig('Bn2.jpg')

e_to_mA2 = 8*math.pi**2 * V/l**2 /(k/1000)**2
sigma_e_to_mA2 = e_to_mA2 * math.sqrt(2) *sigma_k


print(2*e_to_mA*10**(-13), sigma_e_to_mA*10**(-15), 2*e_to_mA2*10**(-13), sigma_e_to_mA2)




