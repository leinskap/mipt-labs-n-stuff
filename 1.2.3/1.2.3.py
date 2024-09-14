import statistics as st
import numpy as np
import matplotlib.pyplot as plt
i = np.array([9.83, 9.94, 10.29, 10.77, 11.2, 12.19, 12.90, 15.34])
i = i * 10**(-3)
h = np.array([0, 1, 2, 2.5, 3, 4, 4.5, 6])
h = h * 10**(-2)
h2 = [x**2 for x in h]
h2err = np.array([1*10**(-4)]*8)
ierr = np.array([0.1, 0.1, 0.1, 0.11, 0.11, 0.12, 0.13, 0.15])
ierr = ierr * 10**(-3)
fig, ax = plt.subplots()
ax.errorbar(h2, i, xerr=h2err, yerr=ierr, fmt='o', ecolor='red', capsize=2)

coefs = np.polyfit(h2,i,1)
p = np.poly1d(coefs)


ax.scatter(h2, i)
ax.plot(h2, p(h2), c='red')
ax.set_xlabel('$h^2, м^2$')
ax.set_ylabel('$I, кг \cdot м^2$')
print(coefs)
plt.show()