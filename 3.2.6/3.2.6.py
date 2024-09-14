import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import curve_fit

sigma_x = 0.5*10**(-3) #м
sigma_U0 = 1.5/150 #B
U0 = 66/150*3 #В




# определение динамической постоянной
R1toR2 = 1/1000
R2 = 10000 #Ом
R0 = 500 #Ом
x = np.array([24.4, 21.5, 17.9, 17.3, 16.6, 16, 15.5, 13.6, 12.2, 7.6, 4.8])
x = x*10
R = np.array([8.8999, 10, 12, 12.5, 13, 13.5, 14, 16, 18, 30, 50])
I = np.array([R1toR2*U0/(z*1000+R0) for z in R])
I *= 10**9
sigma_I = I*math.sqrt((sigma_U0/U0)**2 + 0.02**2)

print("I: ", I)
print("sigma_I: ", sigma_I)


fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('Координата светового пятна x, мм')
ax.set_ylabel('Сила тока чере гальванометр I, нА')
# ax.set_title('Зависимость I(x)')

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

ax.scatter(x, I, c='black')
coefs = np.polyfit(x, I, 1)
p = np.poly1d(coefs)

CI = 2*1.41*coefs[0]
SI = 1/CI

sigma_Itox = 1 / math.sqrt(len(I)) * math.sqrt(abs((st.mean(I ** 2) - (st.mean(I)) ** 2) / (st.mean(x ** 2) - (st.mean(x)) ** 2) - coefs[0] ** 2))
sigma_CI = CI* math.sqrt((0.002/141)**2+(sigma_Itox/coefs[0])**2)
ax.plot(x, p(x), label='$\\frac{I}{x}$ = ' + str(round(coefs[0], 2)) + ' ' + u"\u00B1" + ' ' + str(round(sigma_Itox, 2)) + ' $\\frac{нА}{мм}$')


print("CI = ", CI, "нА*м/мм ", u"\u00B1", " ", sigma_CI)
print("SI = ", SI, "мм/нА*м ", u"\u00B1", " ", sigma_CI/CI * SI)

ax.legend()
plt.savefig("I(x).png")
#plt.show()



theta0 = math.log(17.2/1.9)
T0 = 7
print("theta0 = ", theta0, 1/19, T0)


R = np.array([80, 70, 60, 50, 45, 40, 35, 30])
R *= 1000
xn = np.array([21.7, 18.2, 21.4, 16.3, 18.1, 20.6, 23.6, 15.3])
xn*=10**(-3)
xn1 = np.array([9.3, 7.2, 7.5, 4.9, 4.8, 4.9, 4.6, 2.5])
xn1*=10**(-3)
xntoxn1 = np.array([21.7/9.3, 18.2/7.2, 21.4/7.5, 16.3/4.9, 18.1/4.8, 20.6/4.9, 23.6/4.6, 15.3/2.5])
sigma_xntoxn1 = ((sigma_x/xn)**2 + (sigma_x/xn1)**2)**0.5
theta = np.array([math.log(v) for v in xntoxn1])

sigma_theta = sigma_xntoxn1/theta
print("theta = ", theta, sigma_theta)
R_kr = []
for i in range(len(R)):
    R_kr.append((R[i]+R0)/math.sqrt((2*math.pi/theta[i])**2 + 1) - R0)
n = len(R_kr)
R_kr = np.array(R_kr)
sigma_R_kr = 1/(n*(n-1))**0.5 * np.sum((R_kr-st.mean(R_kr))**2)**0.5
print("R_кр", R_kr/1000)
print(st.mean(R_kr)/1000, sigma_R_kr/1000)





x_max = np.array([17.4, 17.5, 17.2, 16.4, 15.6, 13, 11.1, 8.3, 4])
RplusR0 = np.array([50, 45, 40, 30, 20, 15, 10, 5, 2]) + R0/1000
RplusR0 = np.array(RplusR0)
x_max = sorted(x_max)
RplusR0 = sorted(RplusR0)

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlabel('$R+R_0$, кОм')
ax.set_ylabel('Отклонение, см')
# ax.set_title('Зависимость I(x)')

plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()

ax.scatter(RplusR0, x_max, c='black')


xm = 17.2 * math.exp(theta0/4)/math.e
print(xm)
Cq_kr = 2*1.41*1/30*2*10**(-6)*U0/(xm*10)
sigma_Cq = Cq_kr*math.sqrt((sigma_U0/U0)**2 + (0.002/1.41)**2 + (0.1/xm)**2)
print(Cq_kr, sigma_Cq)
tau = R0 * 2 * 10**(-6)
print(tau)
plt.savefig("x(RpR0).png")


