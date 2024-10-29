import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st

SN = 72 # см^2
I = np.array([0.22, 0.59, 1.03, 1.41, 1.78, 2.14, 2.75])
F0 = np.array([0.75, 1.55, 2.6, 3.4, 4.2, 4.9, 6.05])
F = np.array([0.22, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
# for i in range(len(I)):
#     print(I[i], ' & ', F0[i], ' & ', F[i], '\\\\', '\n', '\\hline')



fig, ax = plt.subplots()



x = I
y = (F0 - F)/SN
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]
ax.scatter(x,y)


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$\\frac{B}{I}$ = ' + str(round(m,4)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_m, 4)) + ' $\\frac{мВб}{А \cdot см^2}$')




ax.set_xlabel('I, А')
ax.set_ylabel('B, мВб')




ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

plt.savefig('B(I).png')

# up
fig, ax = plt.subplots()
P = [np.array([0, 5, 19, 50, 85, 122, 157]), np.array([0, -8, -35, -78, -129, -181, -247]), np.array([0, 2, 7, 14, 24, 34, 42]), np.array([0, -1, -4, -6, -11, -17, -21])]
I = [np.array([0, 0.46, 0.95, 1.54, 2.04, 2.52, 2.94]), np.array([0, 0.49, 1.03, 1.55, 2.02, 2.43, 2.95]), np.array([0, 0.46, 1.02, 1.53, 2.03, 2.49, 2.82]), np.array([0, 0.47, 1.06, 1.54, 2.03, 2.48, 3])]
# for j in range(len(P[0])):
#     for i in range(4):
#         print(P[i][j], ' & ', I[i][j], ' & ', end=' ')
#     print('\\\\', '\n', '\\hline')


names = ['$W_1$', '$C_1$', 'Al', 'Cu']
k = np.zeros(len(names))
sigma_k = np.zeros(len(names))
for i in range(len(names)):
    x = p(I[i])**2
    y = P[i]/1000
    coefs = np.polyfit(x, y, 1)
    h = np.poly1d(coefs)
    m = coefs[0]
    ax.scatter(x, y)

    sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
    ax.plot(x, h(x), label=names[i])
    # print(m, sigma_m)
    k[i] = m
    sigma_k[i] = sigma_m
k = k[2:]

sigma_k = sigma_k[2:]
print(k, sigma_k)
d = 1
S = np.pi*d**2/4
nu0 = 1.26*10**(-6)
hi = 2*nu0*k/S
sigma_hi = np.array([hi[i] * math.sqrt((0.01/1)**2 + (sigma_k[i]/k[i])**2 + (0.01/1.26)**2) for i in range(2)])
print(hi*10**6, sigma_hi*10**6)







ax.set_xlabel('$B^2$, $\\frac{мВб^2}{см^2}$')
ax.set_ylabel('$\\Delta P$, г')




ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
# plt.show()
plt.savefig('P(B2).png')
