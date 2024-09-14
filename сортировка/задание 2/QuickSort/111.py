import numpy as np
import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
n = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000])
t = np.array([3816.7, 1668.9, 2419.4, 3480.7, 4481.3, 5328.0, 6407.8, 7578.6, 8708.2])
t2 = np.array([744.9, 1522.9, 2113.1, 3016.2, 4079.5, 4245.7, 4913.3, 6087.1, 7362.9])
t3 = np.array([782.2, 1498.5, 2054.2, 2997.9, 4190.1, 4202.8, 4837.6, 5978.8, 7287.8])

# ax.plot(n,t, c='red')
# ax.plot(n,t2,c='purple')
ax.plot(n,t3, c='orange')
ax.plot(n,t, c='purple')
ax.plot(n,t2, c='red')
print(len(t3))
plt.show()