#импортируем необхрдимые библиотеки
import matplotlib.pyplot as plt
import math

# калибровочные коэффииценты
with open('coefs.txt', 'r') as coefs:
    data = coefs.read().split('\n')
    pk = float(data[0])
    p0 = float(data[1])-37.3

# плотность воздуха
rho = 1.2

# сдвиг оси расстояний
x = [(i-450)*0.0555556 for i in range(100, 900)][::8]

# 00 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
with open('00 mm.txt', 'r') as data00:
    p00 = [float(x)*pk+p0 for x in data00.read().split('\n')]
print(p00)
for i in range(100):
    if p00[i] < 0:
        p00[i] = 0

#скорости
v00 = [(rho*pressure)**0.5 for pressure in p00]

#расход 00
q00 = 0
for i in range(99):
    q00 += 0.5*((abs(x[i]*0.001)*v00[i] + abs(x[i+1]*0.001)*v00[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
q00 = 2*math.pi*q00*rho


# 01 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
with open('10 mm.txt', 'r') as data10:
    p10 = [float(x)*pk+p0 for x in data10.read().split('\n')]
v10 = [(rho*pressure)**0.5 for pressure in p10]
for i in range(100):
    if p10[i] < 0:
        p10[i] = 0

#скорости
v10 = [(rho*pressure)**0.5 for pressure in p10]

#расход 10
q10 = 0
for i in range(99):
    q10 += 0.5*((abs(x[i]*0.001)*v10[i] + abs(x[i+1]*0.001)*v10[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
q10 = 2*math.pi*q10*rho



# # 20 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('20 mm.txt', 'r') as data20:
#     p20 = [float(x)*pk+p0 for x in data20.read().split('\n')]
# v20 = [(rho*pressure)**0.5 for pressure in p20]
# for i in range(100):
#     if p20[i] < 0:
#         p20[i] = 0
#
# #скорости
# v20 = [(rho*pressure)**0.5 for pressure in p20]
# #расход 20
# q20 = 0
# for i in range(99):
#     q20 += 0.5*((abs(x[i]*0.001)*v20[i] + abs(x[i+1]*0.001)*v20[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q20 = 2*math.pi*q20*rho
#
#
# # 30 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('30 mm.txt', 'r') as data30:
#     p30 = [float(x)*pk+p0 for x in data30.read().split('\n')]
# v30 = [(rho*pressure)**0.5 for pressure in p30]
# for i in range(100):
#     if p30[i] < 0:
#         p30[i] = 0
#
# #скорости
# v30 = [(rho*pressure)**0.5 for pressure in p30]
# #расход 30
# q30 = 0
# for i in range(99):
#     q30 += 0.5*((abs(x[i]*0.001)*v30[i] + abs(x[i+1]*0.001)*v30[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q30 = 2*math.pi*q30*rho
#
#
#
# # 40 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('40 mm.txt', 'r') as data40:
#     p40 = [float(x)*pk+p0 for x in data40.read().split('\n')]
# v40 = [(rho*pressure)**0.5 for pressure in p40]
# for i in range(100):
#     if p40[i] < 0:
#         p40[i] = 0
#
# #скорости
# v40 = [(rho*pressure)**0.5 for pressure in p40]
# #расход 40
# q40 = 0
# for i in range(99):
#     q40 += 0.5*((abs(x[i]*0.001)*v40[i] + abs(x[i+1]*0.001)*v40[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q40 = 2*math.pi*q40*rho
#
#
# # 50 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('50 mm.txt', 'r') as data50:
#     p50 = [float(x)*pk+p0 for x in data50.read().split('\n')]
# v50 = [(rho*pressure)**0.5 for pressure in p50]
# for i in range(100):
#     if p50[i] < 0:
#         p50[i] = 0
#
# #скорости
# v50 = [(rho*pressure)**0.5 for pressure in p50]
# #расход 50
# q50 = 0
# for i in range(99):
#     q50 += 0.5*((abs(x[i]*0.001)*v50[i] + abs(x[i+1]*0.001)*v50[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q50 = 2*math.pi*q50*rho
#
#
# # 60 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('60 mm.txt', 'r') as data60:
#     p60 = [float(x)*pk+p0 for x in data60.read().split('\n')]
# v60 = [(rho*pressure)**0.5 for pressure in p60]
# for i in range(100):
#     if p60[i] < 0:
#         p60[i] = 0
# #скорости
# v60 = [(rho*pressure)**0.5 for pressure in p60]
# #расход 60
# q60 = 0
# for i in range(99):
#     q60 += 0.5*((abs(x[i]*0.001)*v60[i] + abs(x[i+1]*0.001)*v60[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q60 = 2*math.pi*q60*rho
#
#
# # 70 mm ----------------------------------------------------------------------------------------------------------------------------------------------------------
# with open('70 mm.txt', 'r') as data70:
#     p70 = [float(x)*pk+p0 for x in data70.read().split('\n')]
# v70 = [(rho*pressure)**0.5 for pressure in p70]
# for i in range(100):
#     if p70[i] < 0:
#         p70[i] = 0
#
# #скорости
# v70 = [(rho*pressure)**0.5 for pressure in p70]
# #расход 70
# q70 = 0
# for i in range(99):
#     q70 += 0.5*((abs(x[i]*0.001)*v70[i] + abs(x[i+1]*0.001)*v70[i+1])*(abs(abs(x[i+1]*0.001)-abs(x[i]*0.001))))
# q70 = 2*math.pi*q70*rho
# print(q70)
#

q = [q00, q10]
s=[]
for i in range(99):
    if v00[i]-v00[i+1]!=0:
        s.append(abs(v00[i]-v00[i+1]))
print(min(s))

s10=[]
for i in range(99):
    if v10[i]-v10[i+1] != 0 and v10[i]<5:
        s10.append(abs(v10[i]-v10[i+1]))
print(min(s10))



# строим график
def cm_to_inch(value):
    return value/2.54
fig, ax = plt.subplots(figsize=(cm_to_inch(20),cm_to_inch(15)))
ax.plot(x, v00, label='Q(00 мм) = ' + str(round(q00*1000, 2)) + '(г/с)')
ax.plot(x, v10, label='Q(10 мм) = ' + str(round(q10*1000, 2)) + '(г/с)')
# ax.plot(x, v20, label='Q(20 мм) = ' + str(round(q20*1000, 2)) + '(г/с)')
# ax.plot(x, v30, label='Q(30 мм) = ' + str(round(q30*1000, 2)) + '(г/с)')
# ax.plot(x, v40, label='Q(40 мм) = ' + str(round(q40*1000, 2)) + '(г/с)')
# ax.plot(x, v50, label='Q(50 мм) = ' + str(round(q50*1000, 2)) + '(г/с)')
# ax.plot(x, v60, label='Q(60 мм) = ' + str(round(q60*1000, 2)) + '(г/с)')
# ax.plot(x, v70, label='Q(70 мм) = ' + str(round(q70*1000, 2)) + '(г/с)')
ax.legend()
ax.set_xlabel('Расстояние от центра струи до трубки Пито, мм')
ax.set_ylabel('Скорость, м/с')
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
plt.show()
