import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st

cu = [3.160, 6.300, 9.486, 12.66, 15.81, 18.98, 22.12, 25.27, 28.51]
al = [4.261, 8.540, 12.78, 17.04, 21.30, 25.55, 29.79, 34.03, 38.26]
fe = [4.125, 8.275, 12.38, 16.51, 20.63, 24.75, 28.86, 32.99, 37.08]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

coefs_cu = np.polyfit(n, cu,1)
p_cu = np.poly1d(coefs_cu)

coefs_al = np.polyfit(n, al,1)
p_al = np.poly1d(coefs_al)

coefs_fe = np.polyfit(n, fe,1)
p_fe = np.poly1d(coefs_fe)


def cm_to_inch(value):
    return value/2.54
fig, ax = plt.subplots(figsize=(cm_to_inch(20),cm_to_inch(15)))
ax.scatter(n, cu, label='Медь, $f_n$ = ' + str(round(coefs_cu[0],3)) + '$\cdot$n, кГц')
ax.scatter(n, al, label='Алюминий, $f_n$ = ' + str(round(coefs_al[0],3)) + '$\cdot$n, кГц', marker='D')
ax.scatter(n, fe, label='Сталь, $f_n$ = ' + str(round(coefs_fe[0],3)) + '$\cdot$n, кГц', marker='p')
n=[0]+n
ax.plot(n, p_cu(n))
ax.plot(n, p_al(n))
ax.plot(n, p_fe(n))
ax.legend()

print(2*0.6*coefs_cu[0]*1000)
print(2*0.6*coefs_al[0]*1000)
print(2*0.6*coefs_fe[0]*1000)
rho_cu = [8908, 8706, 8682]
rho_al = [2685, 2692, 2976]
rho_fe = [7821, 7709, 7998]
print(st.mean(rho_cu))
print(st.mean(rho_al))
print(st.mean(rho_fe))
ax.set_xlabel('Гармоника n')
ax.set_ylabel('Резонансная частота $f_n$, кГц ')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
plt.show()
