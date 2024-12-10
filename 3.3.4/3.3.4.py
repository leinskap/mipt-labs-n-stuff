import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.optimize import curve_fit


a = 2
l = 8
L = 15
B = np.array([21.4, 313.9, 472.6, 609.7, 950.7, 1049.5, 1090.7]) # мТл
Im1 = np.array([0, 0.31, 0.46, 0.62, 1.02, 1.35, 1.54]) # A
# for i in range(len(B)):
#       print(B[i], ' & ', Im1[i], '\\\\')
#       print('\\hline')

I0 = np.array([0.13, 0.2, 0.33, 0.6, 0.75, 0.97]) # мА


Im   = [np.array([0.00, 0.15, 0.26, 0.35, 0.47, 0.61, 0.90, 1.11, 1.34, 1.54]),
      np.array([0.00, 0.18, 0.33, 0.51, 0.62, 0.81, 1.08, 1.33, 1.52]),
      np.array([0.00, 0.13, 0.30, 0.44, 0.56, 0.79, 1.05, 1.31, 1.52]),
      np.array([0.00, 0.15, 0.30, 0.470, 0.600, 0.860, 1.110, 1.370, 1.520]),
      np.array([0.00, 0.13, 0.290, 0.460, 0.580, 0.820, 1.060, 1.330, 1.520]),
      np.array([0.00, 0.140, 0.280, 0.460, 0.590, 0.820, 1.020, 1.310, 1.520])]   #мА
U_34 = [np.array([1.16, 1.67, 1.96, 2.17, 2.45, 2.72, 3.22, 3.41, 3.58, 3.69]),
      np.array([1.74, 2.54, 3.16, 3.75, 4.05, 4.52, 4.99, 5.26, 5.42]),
      np.array([2.87, 3.83, 5.01, 5.79, 6.40, 7.34, 8.08, 8.58, 8.87]),
      np.array([5.25, 7.20, 9.11, 10.77, 11.90, 13.69, 14.87, 15.64, 16.00]),
      np.array([6.55, 8.76, 11.16, 13.35, 14.56, 16.70, 18.17, 19.27, 19.83]),
      np.array([8.46, 11.46, 14.29, 17.24, 18.94, 21.63, 23.10, 24.66, 25.39])]  #мВ

# for i in I0:
#       print('\\multicolumn{2}{|c}{', i,'} & ', end='')
# print('\n')
# print('\\hline')
# for i in range(len(Im[1])):
#       for j in range(len(Im)):
#             if j+1==len(Im):
#                   print(Im[j][i],' & ', U_34[j][i], ' \\\\ ', end='')
#                   break
#             print(Im[j][i], ' & ', U_34[j][i], ' & ', end='')
#       print('\n')
#       print('\\hline')

# Поворот на 180
I_max = 0.97
Im_rot = np.array([0, 0.15, 0.3, 0.43, 0.6, 0.79, 1.11, 1.38, 1.51])
U_34_rot = np.array([7.52, 4.49, 1.86, 0.15, -2.01, -3.73, -5.71, -6.76, -7.15])

# Первый образец - дырочная проводимость

# Определение удельной проводимости
# I = I_max
U_35 = 0.17 # B

# Германий
I_ge = 1
I_m_ge = np.array([0, 0.12, 0.34, 0.54, 0.85, 1.02, 1.29, 1.50])
U_ge_34 = np.array([0.038, 0.02, -0.02, -0.06, -0.11, -0.13, -0.15, -0.16])
U_ge_35 = 1.74 # mV





# Обработка

# В(I_m)
fig, ax = plt.subplots(figsize=(8,6))
x = Im1
y = B
ax.scatter(x, y)
ax.set_xlabel('$I_М$, A')
ax.set_ylabel('B, мТл')

def func(t,a,b):
    return 21.4 + a*t**2+b*t
popt, pcov = curve_fit(func, x, y, maxfev=5000, method='dogbox')
print(popt)


ax.scatter(x,y)

X = np.linspace(min(x), max(x), 100)
ax.plot(X, func(X, *popt))

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
plt.savefig('B(I_m).png')



#-------------------------------------------------------------------------------------------------------------------
K = []
fig, ax = plt.subplots(figsize=(8,6))
for i in range(len(I0)):
      u = U_34[i][1:] + U_34[i][0]
      b = func(Im[i][1:], *popt)
      x = b
      y = u
      ax.scatter(x, y)
      coefs = np.polyfit(x[0:4], y[0:4], 1)
      p = np.poly1d(coefs)
      m = coefs[0]
      K.append(m)

      sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
            abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
      ax.plot(x, p(x), label = str(I0[i]) + ' мА')


plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.legend()
ax.set_xlabel('B, мТл')
ax.set_ylabel('$\\varepsilon_x$, мВ')
plt.savefig('E(B).png')
# print(I0)
# print([round(float(k), 2) for k in K])

# for i in range(len(I0)):
#       print(I0[i], ' & ', end=' ')
# print('\\\\', '\n', '\\hline')
# for k in K:
#       print(round(float(k),2), ' & ', end=' ')
# print('\\\\', '\n', '\\hline')


fig, ax = plt.subplots(figsize=(8,6))

x = I0
y = np.array(K)
ax.scatter(x, y)
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]

sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
      abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x))


plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_xlabel('$I_0$, мА')
ax.set_ylabel('$K$, $\\frac{В}{Тл}$')

plt.savefig('K(I).png')


e = 1.6*10**(-19)

R_H = m*a # м^3/Кл
print(m)

n = 1/(R_H*e)

sigma = 0.97*L/(U_35*a*l) # 1/(Ом * м)

b = sigma/(e*n)
print('R_H', R_H, 'n', n, 'sigma', sigma, 'b', b)

# plt.show()

