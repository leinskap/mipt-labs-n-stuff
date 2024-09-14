import numpy as np
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
n = np.array([20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
t = np.array([2438.37, 3812.91, 5234.02, 6690.77, 8053.33, 9686.87, 11127.6, 12398.3, 14179])
nlogn = np.array([x*math.log2(x) for x in n])
tnlogn = t
for i in range(9):
    tnlogn[i] = t[i]/(n[i]*math.log2(n[i]))
ax.set_ylim(0,0.05)
ax.set_xlim(15000,105000)
ax.set_yscale('linear')
ax.set_ylabel('t/N*log2(N)')
ax.set_xlabel('N')
ax.scatter(n, tnlogn, color='red', linewidths=1)
coefs = np.polyfit(n,tnlogn,1)
p = np.poly1d(coefs)
ax.plot(n,p(n), c='red')

plt.show()