import matplotlib.pyplot as plt
import math
import numpy as np
nu = np.array([1, 5, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 20000000, 30000000])
uac = np.array([1.4, 4.2, 5, 6, 6, 6, 6, 6, 4.8, 4.1, 3.4])
udc = np.array([5, 5, 5, 6, 6, 6, 6, 6, 4.8, 4.1, 3.4])

lgnu = [round(math.log(x, 10), 3) for x in nu]
kac = [round(x/6, 3) for x in uac]
kdc = [round(x/6, 3) for x in udc]

plt.plot(lgnu, kac, linestyle='-.', marker='o', linewidth=2.5, label='AC')
plt.plot(lgnu, kdc, marker='^', label='DC')
plt.xlabel("lg ν")
plt.ylabel("K")
plt.legend()
plt.show()



