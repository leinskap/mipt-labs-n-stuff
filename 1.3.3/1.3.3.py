import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as st
d1 = 4.1*10**(-3)
d2 = 3*10**(-3)
d3 = 5.2*10**(-3)
r = np.array([d1/2, d2/2, d3/2])
T = 273+25.3
p0 = 97490
M = 28.97 * 10**(-3)
rho = M*p0/(8.31*T)
sigma_rho = rho * ((0.4/25.3)**2 + (3/974.9)**2)**0.5
print('rho = ', rho, u"\u00B1", sigma_rho)
Q_kr = np.array([(math.pi*x*1000*2*10**(-5))/rho for x in r])
print(Q_kr*3600000)
dP_kr = []
for i in range(3):
    dP_kr.append((8*2*10**(-5)*0.5*Q_kr[i])/(math.pi * r[i]**4))
print(dP_kr)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## зависимость перепада давления dP от расхода Q
def pa(n, k):
    return k*n*9.80665
## ламинарное течение, 4.1 мм
Q1 = np.array(sorted([32.4, 167.4, 205.2, 243, 216, 77.4, 306]))
n = np.array(sorted([6, 32, 39, 49, 42, 15, 63]))
n1 = pa(n, 0.2)

## турбулентное течение, 4.1 мм
Q2 = np.array(sorted([464.4, 480.6, 513, 514.8, 540, 556.2, 572.4]))
n = np.array(sorted([159, 171, 187, 189, 209, 217, 234]))
n2 = pa(n, 0.2)


fig, ax = plt.subplots(2,1, figsize=(7,10))
coefs = np.polyfit(n1, Q1,1)


def f1(x):
    return coefs[0]*x+coefs[1]
x = np.linspace(0, 200, 2)
ax[0].plot(x, f1(x), c='red')

coefs1 = np.polyfit(n2, Q2,1)
p1 = np.poly1d(coefs1)

def f2(x):
    return coefs1[0]*x+coefs1[1]
x = np.linspace(100, 550, 2)
ax[0].plot(x, f2(x), c='red')

k = coefs[0]/3600000
eta1 = math.pi*r[0]**4/(8*0.5*k)
sigma_k = 0.02*k
sigma_r = 0.05
sigma_eta1 = eta1*(4*(sigma_r/4.1)**2+0.02**2)**0.5
print('eta1 = ', eta1, u"\u00B1", sigma_eta1)
print('epsilon_eta1 = ', (4*(sigma_r/4.1)**2+0.02**2)**0.5)



dP_kr = (coefs1[1]-coefs[1])/(coefs[0]-coefs1[0])
Q_kr = coefs[0]*dP_kr+coefs[1]
sigma_Q_kr = Q_kr * (0.02**2+0.02**2)**0.5
print('Q_kr = ', Q_kr, u"\u00B1", sigma_Q_kr)
print('epsilon_Q_kr = ', (0.02**2+0.02**2)**0.5)



Re = Q_kr*rho/(3600000*math.pi*r[0]*eta1)
sigma_Re = Re * ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.1/3)**2 + (sigma_eta1/eta1)**2)**0.5
print('Re1 = ', Re, u"\u00B1", sigma_Re)
print('epsilon Re = ', ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.1/3)**2 + (sigma_eta1/eta1)**2)**0.5)



ax[0].scatter(1,1, c='white', label='$Q_{кр}$ = ' + str(round(Q_kr,1)) + '$\pm$' + str(round(sigma_Q_kr,1)) + ' $\\frac{л}{ч}$')
ax[0].scatter(n1, Q1, label='Ламинарное течение')
ax[0].scatter(n2, Q2, marker='>', label='Турбулентное течение')
ax[0].set_ylabel('Q, $\\frac{л}{ч}$')
ax[0].set_xlabel('$\Delta$P, Па')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость расхода Q от перепада давления $\Delta$P, d = 4.1 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)

l_ust = 0.2 * r[0] * Re
print('l1= ', l_ust)
plt.savefig('4.1 Q(P).png')




print('\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ламинарное течение, 3.0 мм
Q1 = np.array(sorted([261.8, 213, 18.8, 44.78, 72.9, 104.68, 128.14, 166.2, 141.7]))
n = np.array(sorted([110, 88, 7, 17, 28, 40.5, 49, 70, 58.5]))
n1 = pa(n, 0.3)

## турбулентное течение, 3.0 мм
Q2 = np.array(sorted([341, 329.01, 310.0, 361.2, 365, 391.9, 394.4]))
n = np.array(sorted([187, 160, 144, 206, 216, 258, 265]))
n2 = pa(n, 0.3)

fig, ax = plt.subplots(2,1, figsize=(7,10))
coefs = np.polyfit(n1, Q1,1)


def f1(x):
    return coefs[0]*x+coefs[1]
x = np.linspace(0, 500, 2)
ax[0].plot(x, f1(x), c='red')

coefs1 = np.polyfit(n2, Q2,1)


def f2(x):
    return coefs1[0]*x+coefs1[1]
x = np.linspace(200, 800, 2)
ax[0].plot(x, f2(x), c='red')

k = coefs[0]/3600000
eta2 = math.pi*r[1]**4/(8*0.5*k)
sigma_k = 0.02*k
sigma_r = 0.1
sigma_eta2 = eta2*(4*(sigma_r/3)**2+0.02**2)**0.5
print('eta2 = ', eta2, u"\u00B1", sigma_eta2)
print('epsilon_eta2 = ', (4*(sigma_r/3)**2+0.02**2)**0.5)



dP_kr = (coefs1[1]-coefs[1])/(coefs[0]-coefs1[0])
Q_kr = coefs[0]*dP_kr+coefs[1]
sigma_Q_kr = Q_kr * (0.02**2+0.02**2)**0.5
print('Q_kr = ', Q_kr, u"\u00B1", sigma_Q_kr)



Re = Q_kr*rho/(3600000*math.pi*r[1]*eta2)
sigma_Re = Re * ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.1/3)**2 + (sigma_eta2/eta2)**2)**0.5
print('Re2 = ', Re, u"\u00B1", sigma_Re)
print('epsilon Re = ', ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.1/3)**2 + (sigma_eta2/eta2)**2)**0.5)



ax[0].scatter(1,1, c='white', label='$Q_{кр}$ = ' + str(round(Q_kr,1)) + '$\pm$' + str(round(sigma_Q_kr,1)) + ' $\\frac{л}{ч}$')
ax[0].scatter(n1, Q1, label='Ламинарное течение')
ax[0].scatter(n2, Q2, marker='>', label='Турбулентное течение')
ax[0].set_ylabel('Q, $\\frac{л}{ч}$')
ax[0].set_xlabel('$\Delta$P, Па')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость расхода Q от перепада давления $\Delta$P, d = 3.0 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)

l_ust = 0.2 * r[1] * Re
print('l2= ', l_ust)
plt.savefig('3.0 Q(P).png')
print('\n')




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ламинарное течение, 5.2 мм
Q1 = np.array(sorted([251, 349, 125.4, 208.2, 297, 432.6, 399.8]))
n = np.array(sorted([15, 22, 6, 12, 19, 28, 27]))
n1 = pa(n, 0.2)

## турбулентное течение, 5.2 мм
Q2 = np.array(sorted([597.6, 588.6, 506.2, 539.1, 486.5, 563]))
n = np.array(sorted([61, 59, 40, 47, 34, 52]))
n2 = pa(n, 0.2)


fig, ax = plt.subplots(2,1, figsize=(7,10))
coefs = np.polyfit(n1, Q1,1)


def f1(x):
    return coefs[0]*x+coefs[1]
x = np.linspace(0, 70, 2)
ax[0].plot(x, f1(x), c='red')

coefs1 = np.polyfit(n2, Q2,1)


def f2(x):
    return coefs1[0]*x+coefs1[1]
x = np.linspace(50, 130, 2)
ax[0].plot(x, f2(x), c='red')


k = coefs[0]/3600000
eta3 = math.pi*r[2]**4/(8*0.5*k)
sigma_k = 0.02*k
sigma_r = 0.05
sigma_eta3 = eta3*(4*(sigma_r/5.2)**2+0.02**2)**0.5
print('eta3 = ', eta3, u"\u00B1", sigma_eta3)
print('epsilon_eta3 = ', (4*(sigma_r/5.2)**2+0.02**2)**0.5)




dP_kr = (coefs1[1]-coefs[1])/(coefs[0]-coefs1[0])
Q_kr = coefs[0]*dP_kr+coefs[1]
sigma_Q_kr = Q_kr * (0.02**2+0.02**2)**0.5
print('Q_kr = ', Q_kr, u"\u00B1", sigma_Q_kr)



Re = Q_kr*rho/(3600000*math.pi*r[2]*eta3)
sigma_Re = Re * ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.05/5.2)**2 + (sigma_eta3/eta3)**2)**0.5
print('Re3 = ', Re, u"\u00B1", sigma_Re)
print('epsilon Re = ', ((sigma_Q_kr/Q_kr)**2 + (sigma_rho/rho)**2 + (0.05/5.2)**2 + (sigma_eta3/eta3)**2)**0.5)



ax[0].scatter(1,1, c='white', label='$Q_{кр}$ = ' + str(round(Q_kr,1)) + '$\pm$' + str(round(sigma_Q_kr,1)) + ' $\\frac{л}{ч}$')
ax[0].scatter(n1, Q1, label='Ламинарное течение')
ax[0].scatter(n2, Q2, marker='>', label='Турбулентное течение')
ax[0].set_ylabel('Q, $\\frac{л}{ч}$')
ax[0].set_xlabel('$\Delta$P, Па')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость расхода Q от перепада давления $\Delta$P, d = 5.2 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)

l_ust = 0.2 * r[2] * Re
print('l3= ', l_ust)
plt.savefig('5.2 Q(P).png')



sigma_k = 0.02*k
sigma_r = 0.05
sigma_l = 0.5 * 10**(-2)
sigma_eta = eta1*((4*sigma_r/5.2)**2+0.02**2)**0.5
print('\n')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## зависимость давления от расстояния
## 4.1 мм
l = 50
dx = np.array([0, 10.5, 40.5, 80.5, 130.5])
dp = np.array([74, 150, 233, 333])
dp = pa(dp, 0.2)
pressure = np.array([p0, p0-pa(74, 0.2), p0-pa(74+76, 0.2), p0-pa(74+76+83, 0.2), p0-pa(74+76+83+100, 0.2)])
fig, ax = plt.subplots(2, 1, figsize=(7, 10))
ax[0].scatter(dx, pressure, label='Экпериментальные точки')
dx1 = dx - dx[-1]
ax[0].plot(dx, pressure[-1]-pa(100, 0.2)*dx1/l, label='Теоритическая зависимость')
ax[0].set_xlabel('Координата x, см')
ax[0].set_ylabel('Давлени P, Па ')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость давления P от расстояния от начала трубки x, d = 4.1 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)
plt.savefig('P(x) 4.1.png')

## 3 мм
l = 30
dx = np.array([0, 10, 30, 60])
dp = np.array([31, 31+15, 31+15+24])
dp = pa(dp, 0.3)
pressure = np.array([p0, p0-pa(31, 0.3), p0-pa(46, 0.3), p0-pa(70, 0.3)])
fig, ax = plt.subplots(2, 1, figsize=(7, 10))
ax[0].scatter(dx, pressure, label='Экпериментальные точки')
dx1 = dx - dx[-1]
ax[0].plot(dx, pressure[-1]-pa(24, 0.3)*dx1/l, label='Теоритическая зависимость')
ax[0].set_xlabel('Координата x, см')
ax[0].set_ylabel('Давлени P, Па ')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость давления P от расстояния от начала трубки x, d = 3.0 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)
plt.savefig('P(x) 3.0.png')



## 5.2 мм
l = 50
dx = np.array([0, 10.5, 40.5, 80.5, 130.5])
dp = np.array([27, 43, 62, 84])
dp = pa(dp, 0.2)
pressure = np.array([p0, p0-pa(27, 0.2), p0-pa(43, 0.2), p0-pa(62, 0.2), p0-pa(84, 0.2)])
fig, ax = plt.subplots(2, 1, figsize=(7, 10))
ax[0].scatter(dx, pressure, label='Экпериментальные точки')
dx1 = dx - dx[-1]
ax[0].plot(dx, pressure[-1]-pa(22, 0.2)*dx1/l, label='Теоритическая зависимость')

ax[0].set_xlabel('Координата x, см')
ax[0].set_ylabel('Давлени P, Па ')
ax[0].legend()
ax[1].set_title("Рис.  . Зависимость давления P от расстояния от начала трубки x, d = 5.2 мм")
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)
plt.savefig('P(x) 5.2.png')


eta = (eta1 + eta2 + eta3)/3
s_eta = eta * math.sqrt((sigma_eta1/eta1)**2 + (sigma_eta2/eta2)**2 + (sigma_eta3/eta3)**2)
print('eta = ', eta, u"\u00B1", s_eta)
lnR = [math.log(x) for x in sorted(r)]
Q = np.array([48.6, 154.2, 468.9])
# lnR = [math.log(r[1]), math.log(r[2])]
Q /=3600000
fig, ax = plt.subplots(2, 1, figsize=(7, 10))
lnQ = [math.log(x) for x in sorted(Q)]
ax[0].scatter(lnR, lnQ)
coefs = np.polyfit(lnR,lnQ,1)
p = np.poly1d(coefs)
ax[0].plot(lnR, p(lnR), label='Ламинарное течение', linestyle='-.')
print(coefs[0])


Q = np.array([307.7, 637.3])
# lnR = [math.log(x) for x in sorted(r)]
lnR = [math.log(r[1]), math.log(r[0])]
Q /=3600000
lnQ = [math.log(x) for x in sorted(Q)]
ax[0].scatter(lnR, lnQ)
coefs = np.polyfit(lnR,lnQ,1)
p = np.poly1d(coefs)
ax[0].plot(lnR, p(lnR), label='Турбулентное течение')
print(coefs[0])
ax[0].set_xlabel('$\ln{r}$')
ax[0].set_ylabel('$\ln{Q}$')
ax[1].scatter(1, 1, c='white')
ax[1].set_title('Рис.  . Зависимость $\ln{Q}(\ln{r})$')
ax[1].xaxis.set_visible(False)
ax[1].yaxis.set_visible(False)
ax[0].legend()
plt.savefig('lnQ(lnR).png')

