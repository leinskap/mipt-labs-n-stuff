#импортируем необхрдимые библиотеки
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
#задаём пустые массивы
data0 = []
data60 = []

#считываем данные из файлов
with open("00 Pa.txt", 'r') as data:
    data0 = data.read().split("\n")
    data0 = [int(x) for x in data0]
with open("60 Pa.txt", 'r') as data:
    for i in range(500):
        data60.append(int((data.readline().split(" "))[1]))

#данные для построения графика
mean = [st.mean(data0), st.mean(data60)]
pressure = [0, 60]

#расчитываем коэффициеты по методу наименьших квадратов
coefs = np.polyfit(mean, pressure,1)
p = np.poly1d(coefs)

# записываем коэффициенты в файл
with open('coefs.txt', 'w') as c:
    c.write(str(round(coefs[0],2)))
    c.write('\n')
    c.write(str(round(coefs[1],2)))

#строим график
def cm_to_inch(value):
    return value/2.54
fig, ax = plt.subplots(figsize=(cm_to_inch(20),cm_to_inch(15)))
ax.plot(mean,p(mean), c='coral', label = 'P =' + str(round(coefs[0],2)) + '$\cdot$' + 'N' + str(round(coefs[1],2)) + ' ' + '(Па)' )
ax.scatter(mean, pressure, label = 'Измерения', c = 'royalblue')
ax.set_ylabel('Разность давлений в трубке и в струе, Па')
ax.set_xlabel('Отсчёты АЦП')
plt.legend()
plt.title('Калибровочный график \n зависимости показаний АЦП от давления')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
plt.show()