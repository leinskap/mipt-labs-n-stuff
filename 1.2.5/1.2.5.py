import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import math
l=0.122
m = [0.093, 0.116, 0.138, 0.174, 0.214]
M = [x*l for x in m]
w = [0.064, 0.079, 0.095, 0.12, 0.147]
coefs = np.polyfit(m,w,2)
p = np.poly1d(coefs)

fig, ax = plt.subplots()
ax.scatter(m,w)
ax.set_xlabel('Момент приложенной силы $M$,  $кг \cdot$ $м^2$')
ax.set_ylabel("Угловая скорость прецессии $\Omega$, $рад/c$")
ax.plot(m,p(m), c='coral')
ax.grid(True)
plt.show()
# T1 = [46.5, 47, 47, 46, 47]
# print(math.sqrt(( (T1[0]-st.mean(T1))**2 + (T1[1]-st.mean(T1))**2 + (T1[2]-st.mean(T1))**2 + (T1[3]-st.mean(T1))**2 + (T1[4]-st.mean(T1))**2 ))/20)
#
# T2 = [72, 73, 72.4, 73.2, 72.8]
# print(math.sqrt(( (T2[0]-st.mean(T2))**2 + (T2[1]-st.mean(T2))**2 + (T2[2]-st.mean(T2))**2 + (T2[3]-st.mean(T2))**2 + (T2[4]-st.mean(T2))**2 ))/20)
#
# T3 = [80.7, 81.3, 80.6, 80.9]
# print(math.sqrt(( (T3[0]-st.mean(T3))**2 + (T3[1]-st.mean(T3))**2 + (T3[2]-st.mean(T3))**2 + (T3[3]-st.mean(T3))**2 ))/12)
#
# T4 = [86, 87, 85.9, 85.7, 86.1]
# print(math.sqrt(( (T4[0]-st.mean(T4))**2 + (T4[1]-st.mean(T4))**2 + (T4[2]-st.mean(T4))**2 + (T4[3]-st.mean(T4))**2 + (T4[4]-st.mean(T4))**2 ))/20)
#
# T5 = [72, 73, 72.4, 73.2, 72.8]
# print(math.sqrt(( (T5[0]-st.mean(T5))**2 + (T5[1]-st.mean(T5))**2 + (T5[2]-st.mean(T5))**2 + (T5[3]-st.mean(T5))**2 + (T5[4]-st.mean(T5))**2 ))/20)
