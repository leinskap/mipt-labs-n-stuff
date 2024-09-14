import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

def speedOfSound_experiment(data_0, data_1): #'rcgthbvtynfkmyfz crjhjcnm

    SamplingRate = 500000 # Частота дискретизации
    L = 1.158 # расстояние между микрофонами

    max_ob0 = max(data_0)
    max_ind0 = data_0.index(max_ob0)

    max_ob1 = max(data_1)
    max_ind1 = data_1.index(max_ob1)
    #print(max_ind0 , max_ind1)
    t = (abs((max_ind1 - max_ind0))/SamplingRate)+0.000155

    return (L / t)

def speedOfSound_theory(temp, fi):#теоретическое значение скорости звука
#           H2O    N2+O2+Ar   CO2
    Mi = [0.01801, 0.02897, 0.04401]  #молярная масса 
    Cpi = [1.863, 1.0036, 0.838]
    Cvi = [1.403, 0.7166, 0.649]
    R = 8.314

    array_a = []
    array_x = []

    x = 0 # Концентрация CO2
    for i in range(0, 100):
        x += 0.001
        M = ( fi * (Mi[0]-Mi[1]) + x * (Mi[2]-Mi[1]) + Mi[1] )
        Y = ( fi * (Mi[0] * Cpi[0] - Mi[1] * Cpi[1]) + x * (Mi[2] * Cpi[2] - Mi[1] * Cpi[1]) + Mi[1] * Cpi[1] ) / ( fi * (Mi[0] * Cvi[0] - Mi[1] * Cvi[1]) + x * (Mi[2] * Cvi[2] - Mi[1] * Cvi[1]) + Mi[1] * Cvi[1] )
        a = ( Y * R * temp / M ) ** 0.5
        array_a.append(a)#скорость при текущей концентрации
        array_x.append(x*100)#концентрация
    return array_a, array_x

def grafics(x, y, a):
    x = np.array(x)
    y = np.array(y)

    fig, ax = plt.subplots()

    ax.plot(x, y, label="Теор зависимость",
            marker="", linestyle="-",
            color='green', linewidth=1)

    array_a_get = []

    ax.plot(1.7, a, label=" 370.5 [м/с], 1.7 [%]",
            marker="o", linestyle="",
            color='blue', linewidth=1)

    ax.grid(which = "major", linewidth = 1)
    ax.grid(which = "minor", linewidth = 0.2)
    ax.minorticks_on()
    plt.text(0, 358, 'Влажность 41,9 %\nТемпература  25,3 по Цельсии', 
             bbox={"facecolor": "white",
                   "edgecolor": "black"}, size=7)

    plt.xlabel("Концентрация CO2 [%]", size=10)
    plt.ylabel("Скорость звука [м/с]", size=10)
    plt.legend()
    plt.show()
    # Сохраним график
    fig.savefig('SoundSpeedair.png', dpi=600)

# наши параметры
temp = 25.3
temp += 273 # в Кельвинах
fi = 41.9
fi /= 100

# считываем данные
with open ("data_0_air2.txt", 'r') as file:
    data_0_air = []
    for f in file:
        data_0_air.append(f.split()[0])

with open ("data_1_air2.txt", 'r') as file:
    data_1_air = []
    for f in file:
        data_1_air.append(f.split()[0])

a_air = speedOfSound_experiment(data_0_air[500:], data_1_air[500:])
print('Скорость звука ', a_air, 'м/с')

array_a, array_x = [], []
array_a, array_x = speedOfSound_theory(temp, fi)

grafics(array_x, array_a, a_air)

