import numpy as np
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
n = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
t = np.array([261.18, 529.95, 846.53, 1170.37, 1458.36, 1789.26, 2054.49, 2474.35, 2755.4, 3151.4])
nlogn = np.array([x*math.log2(x) for x in n])
tnlogn = t
for i in range(10):
    tnlogn[i] = t[i]/(n[i]*math.log2(n[i]))
n=[0]+n
tnlogn=[0]+tnlogn
ax.set_ylim(0,0.01)
ax.set_xlim(0,105000)
ax.set_yscale('linear')
ax.set_ylabel('t/N*log2(N)')
ax.set_xlabel('N')
ax.scatter(n, tnlogn, color='red', linewidths=1)
coefs = np.polyfit(n,tnlogn,1)
p = np.poly1d(coefs)
ax.plot(n,p(n), c='red')

plt.show()