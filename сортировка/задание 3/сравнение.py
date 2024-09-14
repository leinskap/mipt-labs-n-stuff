import numpy as np
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
#n = np.array([512, 1024, 2048, 4096, 8192, 16384, 32768, 65536])
n = n = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
nlogn = np.array([x*math.log2(x) for x in n])

tb = [580.9, 2768.3, 7534.8, 15952.2, 29149.7, 48427.1, 74297.1, 108420.1, 151088.0, 204245.1]
t = [104.33, 221.79, 330.11, 427.15, 550.65, 655.75, 772.9, 925.25, 1034.24, 1155.59]


ax.set_yscale('linear')
ax.set_ylabel('t')
ax.set_xlabel('N')
ax.plot(n, t, color='red', label='Heap Sort')
ax.scatter(n, t, color='red')
ax.scatter(n,tb, color='purple')
ax.plot(n,tb, color='purple', label='Bubble Sort')
# coefs = np.polyfit(n,tb,2)
# p = np.poly1d(coefs)
# ax.plot(n,p(n), c='purple',label='Bubble Sort')
ax.legend()
plt.show()