import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st













d1 = np.array([1.7, 3.5, 4.1, 6.8, 7.5, 9.0, 11.1, 12.8, 13.1, 15, 19.5, 25.2, 30.8])
d2 = np.array([0.155, 0.204, 0.231, 0.3, 0.328, 0.377, 0.432, 0.461, 0.617, 0.672, 0.843, 1.025, 1.182])
d3 = np.array([0.2, 0.5, 0.9, 1.6, 1.9, 2.4, 3, 3.4, 5.2, 5.8, 7.5, 8.5, 11.1])

x = d2
y = d1
fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_xlabel('Датчик 2, $0,1 \cdot мм$')
ax.set_ylabel('Датчик 1, Н')
ax.set_title('')

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$k_{1}$ = ' + str(round(m,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_m, 2)) + ' $\\frac{H}{0,1 \\cdot мм}$')


ax.legend()
plt.savefig('1.png')





x = d2
y = d3
fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_xlabel('Датчик 3, $0,1 \cdot мм$')
ax.set_ylabel('Датчик 1, Н')
ax.set_title('')

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
m = coefs[0]


sigma_m = 1 / math.sqrt(len(x)) * math.sqrt(
        abs((st.mean(y ** 2) - (st.mean(y)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - m ** 2))
ax.plot(x, p(x), label='$k_{2}$ = ' + str(round(m,2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_m, 2)) + ' $\\frac{H}{0,1 \\cdot мм}$')

ax.legend()
plt.savefig('2.png')
plt.show()