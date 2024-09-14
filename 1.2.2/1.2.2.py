import numpy as np
import math
from scipy.optimize import curve_fit
import statistics as st
import matplotlib.pyplot as plt
b0 = [0.3482, 0.6034, 0.669, 1.067, 2.300]
t = [6.1, 9.4, 12, 18.5, 36]
treal = [x*(10**(-3)) for x in t]


average_b0 = st.mean(b0)
b2 = [x**2 for x in b0]
average_b2 = st.mean(b2)
average_t = st.mean(treal)
t2 = [x**2 for x in treal]

average_t2 = st.mean(t2)
# print(average_t, average_t2, average_b0, average_b2)
# print( (1/math.sqrt(5)) * math.sqrt( (average_b2 - average_b0**2)/(average_t2 - average_t**2)-64.95**2) )


# coefs = np.polyfit(t,b0,1)
# p = np.poly1d(coefs)
# print(coefs)
fig, ax = plt.subplots()
# ax.scatter(t,b0)
# ax.plot(t,p(t), c='red')
# ax.set_xlabel('Момент силы натяжения нити, мН*м')
# ax.set_ylabel('Угловое ускорение, рад/с^2')
i = [7, 8.51, 11.64]
r = [9, 25, 64]
rreal = [x*10**(-4) for x in r]
ireal = [x*10**(-3) for x in i]
average_i = st.mean(ireal)
i2 = [x**2 for x in ireal]
average_i2 = st.mean(i2)
average_r2 = st.mean(rreal)
r4 = [x**2 for x in rreal]
average_r4 = st.mean(r4)

print( (1/math.sqrt(3)) * math.sqrt( (average_i2 - average_i**2)/(average_r4 - average_r2**2)-0.836**2) )
print(0.014 * math.sqrt(average_r4-average_r2**2))



coefs = np.polyfit(rreal, ireal, 1)
p = np.poly1d(coefs)
# print(coefs)
coefs = np.polyfit(r, i, 1)
p = np.poly1d(coefs)
ax.scatter(r, i)
ax.plot(r, p(r), color='red')
ax.set_xlabel('Квадрат расстояния R, см^2')
ax.set_ylabel('Момент инерции, г*м^2 ')

# print(st.mean(b0))
# print(math.sqrt( (0.0015 + 0.0012 + 0.0001 + 0.0007 + 0.0001) / 20))

