import numpy as np
import matplotlib.pyplot as plt
import math





fig, ax = plt.subplots()
n = np.array([64, 128, 256, 512, 1024, 2048, 4096, 8192])


##bubble sort
# tb = np.array([10.0, 37.9, 131.9, 452.9, 1631.5, 6205.9, 24724.5, 101952.2])
# tbmin = np.array([6.6, 28.1, 77.7, 261.8, 895.7, 3225.2, 12267.4, 48072.5])
# tbmax = np.array([3.9, 14.0, 57.2, 209.5, 754.6, 2934.5, 11800.4, 46795.4])
# ax.scatter(n, tb, color='red', linewidths=1)



# ##slection sort
ts = np.array([math.log2(x) for x in [4.1, 10.6, 38.3, 119.2, 419.8, 1573.0, 6029.2, 24102.7]])
tsmin =np.array([3.1, 11.1, 34.5, 116.5, 413.7, 1525.7, 5936.4, 23350.2])
ax.scatter(n,ts, color = 'purple',linewidths=1)
#
#
# ##insert sort
# ti = np.array([math.log2(x) for x in [6.8, 21.1, 78.8, 311.5, 1147.4, 4542.5, 17718.8, 71019.5]])
# ax.scatter(n,ti, color = 'orange',linewidths=1)
#
#
#

# lineb, = ax.plot(n,tb, c='red', label='Bubble Sort')
# linebmin, = ax.plot(n,tbmin, c='purple', label='Bubble Sort min')
# linebmax, = ax.plot(n,tbmax, c='blue', label='Bubble Sort max')
lines, = ax.plot(n,ts, c='purple', label='Selection Sort')
linesmin, = ax.plot(n,tsmin, c='purple', label='Selection Sort')
# linei, = ax.plot(n,ti, c='orange', label='Insert Sort')
ax.legend()


ax.set_xlabel('log2(N)')
ax.set_ylabel('log2(t)')
plt.show()