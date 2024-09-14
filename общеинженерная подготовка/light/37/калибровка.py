import matplotlib.pyplot as plt
import numpy as np


# получение коэффициентов калибровки
x = [152, 265]
y = [435.83, 576.96]
coefs = np.polyfit(x,y,1)
p = np.poly1d(coefs)
print(coefs)



# построение графика
fig, ax = plt.subplots()
ax.scatter(x,y, label = '$\lambda$ = ' + str(round(coefs[0],3)) + '$\cdot$ n' + ' + ' + str(round(coefs[1],3)) + ' нм')
ax.plot(x,p(x), c='red')
ax.legend()
ax.set_xlabel('Относительный номер пикселя')
ax.set_ylabel('Длина волны, нм')
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()
plt.savefig('калибровка.png')
plt.show()