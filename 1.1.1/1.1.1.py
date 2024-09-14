import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(0, 350, 350)
x2 = np.linspace(0, 270, 270)
x3 = np.linspace(0, 150, 150)


## длины проволок
l1=0.2 ## м
l2=0.3 ## м
l3=0.5 ## м
sigma_l = 0.5 ## мм


## средний диаметр проволоки(по микрометру)
d=0.354 ## мм
sigma_d = 0.01 ## мм
## внутренне сопротивление вольтметра
R_V = 5000 ## Ом

## массив напряжений
v1 = np.array([39, 41, 43, 70, 111, 129, 61, 51, 38, 35, 30, 28])
v2 = np.array([41, 52, 63, 68, 75, 82, 148, 136, 120, 91, 71, 64])
v3 = np.array([48, 74, 89, 91, 112, 118, 136, 131, 130, 119, 82, 71])
for i in range(0, 12):
    v1[i] *= 5
    v2[i] *= 5
    v3[i] *= 5

## массив токов
i1 = np.array([94.4, 99.3, 107.4, 169.7, 280.7, 315.0, 150.0, 123.5, 92.0, 81.6, 72.2, 67.8])
i2 = np.array([65.1, 82.6, 104.0, 113.8, 124.7, 137.3, 247.6, 226.0, 202.7, 153.3, 118.7, 107.8])
i3 = np.array([43.4, 73.9, 85.0,  89.3, 105.5, 113.6, 131.7, 124.8, 122.8, 112.5, 77.8, 67.5])



## средние сопротивления

vi1=[]
i1SqMean = 0
i1Sq=[]
for i in range(12):
    vi1.append(v1[i]*10**(-3)*i1[i]*10**(-3))
    i1Sq.append((i1[i]*10**(-3))**2)

vi1Mean = sum(vi1)/12
i1SqMean = sum(i1Sq)/12
rMean1 = vi1Mean/i1SqMean


vi2 = []
i2SqMean = 0
i2Sq = []
for i in range(12):
    vi2.append(v2[i]*10**(-3)*i2[i]*10**(-3))
    i2Sq.append((i2[i]*10**(-3))**2)

vi2Mean = sum(vi2)/12
i2SqMean = sum(i2Sq)/12
rMean2 = vi2Mean/i2SqMean


vi3 = []
i3SqMean = 0
i3Sq = []
for i in range(12):
   vi3.append(v3[i]*10**(-3)*i3[i]*10**(-3))
   i3Sq.append((i3[i]*10**(-3))**2)

vi3Mean = sum(vi3)/12
i3SqMean = sum(i3Sq)/12
rMean3 = vi3Mean/i3SqMean
# print(rMean1,rMean2,rMean3)


## сопротивление проволоки (с поправкой)
R_pr1 = rMean1 + (rMean1**2)/R_V
R_pr2 = rMean2 + (rMean2**2)/R_V
R_pr3 = rMean3 + (rMean3**2)/R_V
# print(R_pr1)
# print(R_pr2)
# print(R_pr3)


## случайная погрешность
V1SqMean = sum([(x*10**(-3))**2 for x in v1])/12
I1SqMean = sum([(x*10**(-3))**2 for x in i1])/12
sigma_rnd1 = 1/(12**0.5) * (V1SqMean/I1SqMean - rMean1**2)**0.5


V2SqMean = sum([(x*10**(-3))**2 for x in v2])/12
I2SqMean = sum([(x*10**(-3))**2 for x in i2])/12
sigma_rnd2 = 1/(12**0.5) * (V2SqMean/I2SqMean - rMean2**2)**0.5


V3SqMean = sum([(x*10**(-3))**2 for x in v3])/12
I3SqMean = sum([(x*10**(-3))**2 for x in i3])/12
sigma_rnd3 = 1/(12**0.5) * (V3SqMean/I3SqMean - rMean3**2)**0.5
# print(sigma_rnd1)
# print(sigma_rnd2)
# print(sigma_rnd3)


## систематическая погрешность
sigma_sist1 = rMean1 * ((1.25/max(v1))**2 + (0.65/max(i1))**2)**0.5
sigma_sist2 = rMean2 * ((1.25/max(v2))**2 + (0.65/max(i2))**2)**0.5
sigma_sist3 = rMean3 * ((1.25/max(v3))**2 + (0.65/max(i2))**2)**0.5
# print(sigma_sist1)
# print(sigma_sist2)
# print(sigma_sist3)

## общая ошибка измерения сопротивления


sigma_R1 = (sigma_sist1**2 + sigma_rnd1**2)**0.5
sigma_R2 = (sigma_sist2**2 + sigma_rnd2**2)**0.5
sigma_R3 = (sigma_sist3**2 + sigma_rnd3**2)**0.5

# print(sigma_R1)
# print(sigma_R2)
# print(sigma_R3)



## удельное сопротивление
rho1 = (R_pr1/l1) * ((math.pi * (d*10**(-3))**2)/4) * 10**6
rho2 = (R_pr2/l2) * ((math.pi * (d*10**(-3))**2)/4) * 10**6
rho3 = (R_pr3/l3) * ((math.pi * (d*10**(-3))**2)/4) * 10**6
# print(rho1)
# print(rho2)
# print(rho3)

## погрешность расчета удельного сопротивления
sigma_rho1 = rho1 * ((sigma_R1/R_pr1)**2 + (2*sigma_d/d)**2 + (sigma_l/(l1*1000))**2)**0.5
sigma_rho2 = rho2 * ((sigma_R3/R_pr2)**2 + (2*sigma_d/d)**2 + (sigma_l/(l2*1000))**2)**0.5
sigma_rho3 = rho3 * ((sigma_R3/R_pr3)**2 + (2*sigma_d/d)**2 + (sigma_l/(l3*1000))**2)**0.5
print(sigma_rho1)
print(sigma_rho2)
print(sigma_rho3)


## аппроксимация
y1 = x1*rMean1
y2 = x2*rMean2
y3 = x3*rMean3

## график
fig, ax = plt.subplots()

ax.errorbar(i1, v1, xerr =(0.02*i1+0.02) ,yerr=2.5, capsize=6, fmt=' ', c='black')
ax.scatter(i1,v1, c='black', s=20, marker='o')
ax.plot(x1,y1, c='black')

ax.errorbar(i2, v2, xerr =(0.02*i2+0.02) ,yerr=2.5, capsize=6, fmt=' ', c='green')
ax.scatter(i2,v2, c='green', s=20, marker='o')
ax.plot(x2,y2, c='green')

ax.errorbar(i3, v3, xerr =(0.02*i3+0.02) ,yerr=2.5, capsize=6, fmt=' ', c='orange')
ax.scatter(i3,v3, c='orange', s=20, marker='o')
ax.plot(x3,y3, c='orange')

ax.set_xlabel("I, мА")
ax.set_ylabel("V, мB")

plt.show()