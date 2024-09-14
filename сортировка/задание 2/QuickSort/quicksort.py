import numpy as np
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
n = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
t = np.array([801.9, 1714.5, 2492.2, 3562.7, 4624.7, 5369.9, 6320.7, 7560.0, 8693.0, 9561.8])
nlogn = np.array([x*math.log2(x) for x in n])
tnlogn = t
for i in range(10):
    tnlogn[i] = t[i]/(n[i]*math.log2(n[i]))
n=[0]+n
tnlogn=[0]+tnlogn
ax.set_ylim(0,0.03)
ax.set_xlim(0,105000)
ax.set_yscale('linear')
ax.set_ylabel('t/N*log2(N)')
ax.set_xlabel('N')
ax.scatter(n, tnlogn, color='red', linewidths=1)
coefs = np.polyfit(n,tnlogn,1)
p = np.poly1d(coefs)
ax.plot(n,p(n), c='red')

plt.show()