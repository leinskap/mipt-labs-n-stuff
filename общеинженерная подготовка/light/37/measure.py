import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

photos = ['calibration.png', 'blue.png', 'green.png', 'red.png', 'white.png', 'yellow.png']


# получение данных
rgb, I0 = j.read_image(photos[0], 'graph1.png', 'ртутная лампа', 'белый лист')
I1 = j.read_image(photos[1], 'graph2.png', 'лампа накаливания', 'синий лист')[-1]
I2 = j.read_image(photos[2], 'graph3.png', 'лампа накаливания', 'зеленый лист')[-1]
I3 = j.read_image(photos[3], 'graph4.png', 'лампа накаливания', 'красный лист')[-1]
I4 = j.read_image(photos[4], 'graph5.png', 'лампа накаливания', 'белый лист')[-1]
I5 = j.read_image(photos[5], 'graph6.png', 'лампа накаливая', 'желтый лист')[-1]
I1 = I1[:352]
I2 = I2[:352]
I3 = I3[:352]
I4 = I4[:352]
I5 = I5[:352]
# r = [i[0] for i in rgb]
# b = [i[2] for i in rgb]
# r_max, b_max = max(r), max(b)
# i_r, i_b = r.index(r_max), b.index(b_max)

luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]
print(list(luma).index(max(luma[:180])))
print(list(luma).index(max(luma[250:])))


# калибровка
# a = (546.074 - 435.83)/(i_green - i_blue)
# b = 546.074 - a*i_green

a = 1.249
b = 245.991


# построение графиков
x = np.linspace(0, len(I4), len(I4))
x = [i * a + b for i in x]
plt.cla()
plt.clf()

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.plot(x, I1, color='blue', label='blue')
plt.plot(x, I2, color='green', label='green')
plt.plot(x, I3, color='red', label='red')
plt.plot(x, I4, color='white', label='white')
plt.plot(x, I5, color='yellow', label='yellow')

# for i in range (len(I4)):
#     print(i, ' ', I4[i])



plt.legend()
plt.title('Отражённая интенсивность излучения лампы накаливания')
plt.ylabel('Яркость')
plt.xlabel('Длина волны, нм')
plt.savefig('I.png')

# A1=[]
# for i in range(len(I1)):
#     if I4[i] == 0:
#         A1.append(0)
#     else:
#         A1.append(I1[i] / I4[i])
# A2=[]
# for i in range(len(I1)):
#     if I4[i] == 0:
#         A2.append(0)
#     else:
#         A2.append(I2[i] / I4[i])
# A3=[]
# for i in range(len(I3)):
#     if I4[i] == 0:
#         A3.append(0)
#     else:
#         A3.append(I3[i] / I4[i])
# A4=[]
# for i in range(len(I4)):
#     if I4[i] == 0:
#         A4.append(1)
#     else:
#         A4.append(I4[i] / I4[i])
# A5=[]
# for i in range(len(I5)):
#     if I4[i] == 0:
#         A5.append(0)
#     else:
#         A5.append(I5[i] / I4[i])


# расчёт альбедо
A1 = [I1[i] / I4[i] for i in range(len(I1))]
A2 = [I2[i] / I4[i] for i in range(len(I1))]
A3 = [I3[i] / I4[i] for i in range(len(I1))]
A4 = [I4[i] / I4[i] for i in range(len(I1))]
A5 = [I5[i] / I4[i] for i in range(len(I1))]
# for i in range (len(A5)):
#     print(i, ' ', A5[i])


# построение графиков
plt.cla()
plt.clf()
ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.plot(x, A1, color='blue', label='blue')
plt.plot(x, A2, color='green', label='green')
plt.plot(x, A3, color='red', label='red')
plt.plot(x, A4, color='white', label='white')
plt.plot(x, A5, color='yellow', label='yellow')


plt.legend()
plt.title('Зависимость альбедо поверхностей от длины волны падающего света')
plt.ylabel('Альбедо')
plt.xlabel('Длина волны, нм')
plt.savefig('A.png')
