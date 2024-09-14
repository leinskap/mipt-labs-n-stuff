import numpy as np
import matplotlib.pyplot as plt
import math





fig, ax = plt.subplots()
n = np.array([ 6, 7, 8, 9, 10, 11, 12, 13])


##bubble sort
t = np.array([math.log2(x) for x in [9.6, 35.8, 130.0, 476.8, 1735.5, 6842.1, 28081.3, 118634.5]])
ax.scatter(n, t, color='red', linewidths=1)

t1 = np.array([math.log2(x) for x in [2.4, 9.6, 34.7, 128.2, 486.7, 1810.3, 6872.8, 27130.8]])
ax.scatter(n, t1, color='purple', linewidths=1)


t2 = np.array([math.log2(x) for x in [4, 13.2, 45.1, 160.9, 606.1, 2200.1, 8499.6, 33877.6]])
ax.scatter(n, t2,marker = '^', color='orange', linewidths=1)

t3 = np.array([math.log2(x) for x in [4.0, 13.3, 44.2, 153.8, 608.0, 2266.3, 8679.0, 34404.2]])
ax.scatter(n, t3, color='xkcd:sky blue', linewidths=1)


line, = ax.plot(n, t, c='red', label='Без оптимизации', linewidth='2.5')
line1, = ax.plot(n, t1, c='purple', label='O1', linewidth='2.5')
line2, = ax.plot(n, t2, c='orange', label='O2', linewidth='2.5')
line3, = ax.plot(n, t3, c='xkcd:sky blue', label='O3', linestyle=(0,(5,10)), linewidth='3')
ax.legend()


ax.set_xlabel('log2(N)')
ax.set_ylabel('log2(t)')
plt.show()