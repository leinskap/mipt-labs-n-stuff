import math
import numpy as np
import matplotlib.pyplot as plt
a = np.array([3.1415968, 3.1415968, 3.1415968, 3.1415968])
# x = np.array([math.log10(x) for x in range(10000000000, 10000000004)])
# plt.scatter(x, a,marker='.', linewidths=1)
# plt.xlabel('lg(n)')
# plt.ylabel('f(n)')
# plt.plot(x, [math.pi]*4, color='orange')
# plt.show()
x = np.array([x for x in range(1000000000, 1000000004)])
fig, ax = plt.subplots()
ax.plot(x, [math.pi]*4, color='orange')
ax.scatter(x, a,marker='.', linewidths=3)
ax.ticklabel_format(style='plain', axis='y', useOffset=False)
ax.get_xaxis().set_visible(False)
plt.ylabel('f(n)')
plt.title('log(n)>=9', y=0.1)
plt.show()




























