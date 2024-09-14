#импортируем необхрдимые библиотеки
import numpy as np
import matplotlib.pyplot as plt

#измерения
steps = [0, 900]
distance = [0, 5]

# расчитываем коэффициеты по методу наименьших квадратов
coefs = np.polyfit(steps, distance, 1)
p = np.poly1d(coefs)

#строим графики
def cm_to_inch(value):
    return value/2.54
fig, ax = plt.subplots(figsize=(cm_to_inch(20),cm_to_inch(15)))
ax.plot(steps, p(steps), c='coral', label='x =' + str(round(coefs[0]*10**3, 2)) + '$\cdot 10^{-5}$' + '$\cdot$' + 'n' + ' ' + '(м)')
ax.scatter(steps, distance, label='Измерения', c='royalblue')
ax.set_xlabel('Количество шагов n')
ax.set_ylabel('Перемещение трубки Пито x, см')
plt.title('Калибровочный график \n зависимости перемещения трубки Пито от шага двигателя')
plt.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
plt.show()