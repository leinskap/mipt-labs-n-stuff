import math
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
size = 20 ## размер точки на графике


# 3. Измерения на первой установке (рис. 1).
# a) Исходя из примерного значения скорости звука (300 м/с), рассчитайте, в каком диапазоне частот следует вести
# измерения, чтобы при удлинении трубы можно было наблюдать 2-5 резонансов.
c = 300 # м/с
possibleRangeF = []
for f in range(1000, 10000, 50):
    if (5*c/(2*f)<=0.2):
        possibleRangeF.append(f)
print('---------------------------------------------------------------------------------------------------------', '\n')
print('Пределы измерений: ', min(possibleRangeF),' - ', max(possibleRangeF))
print('---------------------------------------------------------------------------------------------------------', '\n')
print('Воздух')
# б) Измерение скорости звука при помощи раздвижной трубы
# диапазон частот, Гц
fig, ax = plt.subplots(figsize=(8, 5))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('k')
ax.set_ylabel('$\Delta$L, мм')
plt.grid(True, which='major', color='0.8', linestyle='-')
plt.grid(True, which='minor', color='0.85', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
data = [(3290, [33, 86, 137, 191]),
        (3690, [46, 91, 139, 185]),
        (4290, [19, 59, 99, 139, 177]),
        (5190, [27, 60, 93, 126, 159, 193])]
c = []
sigmaDeltaL = 0.7 # мм
waveLen = []
for d in data:
    freq = d[0]
    L = np.array(d[1]) - d[1][0]
    k = np.array([x for x in range(0, len(L))])

    coefs = np.polyfit(k, L, 1)
    p = np.poly1d(coefs)
    a = coefs[0]
    sigma_a = 1 / math.sqrt(len(k)) * math.sqrt(abs(st.mean(L ** 2) / st.mean(k ** 2) - a**2))
    c.append((2 * a * 10 ** (-3) * freq, sigma_a / a * 2 * a * 10 ** (-3) * freq))
    waveLen.append((2 * a, sigma_a))


    ax.scatter(k, L, color='black', s=size)
    ax.plot(k, p(k), label= 'f = ' + str(freq) + ' Гц, ' + 'a = ' + str(round(a, 1)) + u"\u00B1" + ' ' + str(round(sigma_a, 1)) + ' мм', color='0.9', linestyle=':')
    ax.legend()
    plt.savefig('f-воздух.png')

print('Скорость звука в воздухе: ',  round(st.mean([x[0] for x in c]), 1), u"\u00B1", round(min([x[1] for x in c]), 1), 'м/с')
# Показатель адиабаты
M = 28.98 * 10**(-3)
R = 8.314
T = 273.2 + 22.6
sigma_c = min([x[1] for x in c])
c = st.mean([x[0] for x in c])

gamma = M/(R*T) * c**2
sigma_gamma = gamma * math.sqrt(2) * sigma_c/c
# print(waveLen)
print('Показатель адиабаты в воздухе: ',  round(gamma, 3), u"\u00B1", round(sigma_gamma, 3))

# г) Скорость звука в углекислом газе
print('---------------------------------------------------------------------------------------------------------', '\n')
print('Углекислый газ')
fig, ax = plt.subplots(figsize=(8, 5))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('k')
ax.set_ylabel('$\Delta$L, мм')
plt.grid(True, which='major', color='0.8', linestyle='-')
plt.grid(True, which='minor', color='0.85', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
data = [(5190, [6, 32, 58, 84, 110, 137, 164, 190, 216]),
        (4190, [11, 45, 75, 109, 139, 173, 205]),
        (3590, [14, 50, 90, 123, 164, 200])]
c = []
sigmaDeltaL = 0.7 # мм
waveLen = []
for d in data:
    freq = d[0]
    L = np.array(d[1]) - d[1][0]
    k = np.array([x for x in range(0, len(L))])

    coefs = np.polyfit(k, L, 1)
    p = np.poly1d(coefs)
    a = coefs[0]
    sigma_a = 1 / math.sqrt(len(k)) * math.sqrt(abs(st.mean(L ** 2) / st.mean(k ** 2) - a**2))
    c.append((2 * a * 10 ** (-3) * freq, sigma_a / a * 2 * a * 10 ** (-3) * freq))
    waveLen.append((2 * a, sigma_a))

    ax.scatter(k, L, color='black', s=size)
    ax.plot(k, p(k), label='f = ' + str(freq) + ' Гц, ' + 'a = ' + str(round(a, 1)) + u"\u00B1" + ' ' + str(round(sigma_a, 1)) + ' мм', color='0.9', linestyle=':')
    ax.legend()
    plt.savefig('f-CO2.png')

print('Скорость звука в СО2: ',  round(st.mean([x[0] for x in c]), 1), u"\u00B1", round(min([x[1] for x in c]), 1), 'м/с')
# Показатель адиабаты
M = 28.98 * 10**(-3)
R = 8.314
T = 273.2 + 22.6
sigma_c = min([x[1] for x in c])
c = st.mean([x[0] for x in c])

gamma = M/(R*T) * c**2
sigma_gamma = gamma * math.sqrt(2) * sigma_c/c
# print(waveLen)
print('Показатель адиабаты в СО2: ',  round(gamma, 3), u"\u00B1", round(sigma_gamma, 3))


## 4. Измерения на второй установке (постоянная длина трубки)
print('---------------------------------------------------------------------------------------------------------', '\n')
print('Воздух при различных температурах')
fig, ax = plt.subplots(figsize=(6, 8))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('k')
ax.set_ylabel('$\Delta$L, мм')
plt.grid(True, which='major', color='0.8', linestyle='-')
plt.grid(True, which='minor', color='0.85', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
data = [(30, [269, 504, 750, 1000, 1249, 1497]),
        (40, [270, 512, 761, 1061, 1267, 1518]),
        (50, [275, 519, 772, 1031, 1285, 1542]),
        (59, [281, 527, 783, 1045, 1305, 1563])]
# Длина трубки, м
L = 700 * 10**(-3)
sigma_L = 1 * 10**(-3)
gamma = []
sigma_T = 0.1
for d in data:
    T = d[0] + 273.2
    freq = np.array(d[1])
    k = np.array([x for x in range(0, len(freq))])
    freq -= freq[0]

    coefs = np.polyfit(k, freq, 1)
    p = np.poly1d(coefs)
    a = coefs[0]
    sigma_a = 1 / math.sqrt(len(k)) * math.sqrt(abs(st.mean(freq ** 2) / st.mean(k ** 2) - a ** 2))
    # c.append((2 * a * 10 ** (-3) * freq, sigma_a / a * 2 * a * 10 ** (-3) * freq))
    # waveLen.append((2 * a, sigma_a))

    ax.scatter(k, freq, color='black', s=size)
    ax.plot(k, p(k), label='T = ' + str(T) + ' К, ' + 'a = ' + str(round(a, 1)) + u"\u00B1" + ' ' + str(round(sigma_a, 1)) + ' Гц',
            color='0.9', linestyle=':')
    gamma.append((M/(R*T) * 4 * a**2 * L**2,
                  M/(R*T) * 4 * a**2 * L**2 * math.sqrt((sigma_T/T)**2 + 2 * (sigma_L/L)**2 + 2 * (sigma_a/a)**2)))
    ax.legend()
plt.savefig('T.png')
print('Средний показатель адиабаты: ', round(st.mean([x[0] for x in gamma]), 3), u"\u00B1", round(st.mean([x[1] for x in gamma]), 3))



plt.show()


