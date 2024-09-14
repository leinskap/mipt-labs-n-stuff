import matplotlib.pyplot as plt
import numpy as np
import math
nUp = [2.71, 6.1, 9.3, 12.2, 14.8]
nDown = [14.8, 12.1, 9.3, 6, 2.7]
m = [245.3, 489.7, 735.3, 980.9, 1226.2]
m = [i*(10**(-3))*9.807 for i in m]
deltalUp = [i*150/(2*1430) for i in nUp]
deltalDown = [i*150/(2*1430) for i in nDown]

sigmalUp = [deltalUp[i] * math.sqrt( (0.05/nUp[i])**2 + (0.01/0.46)**2 + (0.1/143)**2   ) for i in range(5) ]
sigmalDown = [deltalDown[i] * math.sqrt( (0.05/nDown[i])**2 + (0.01/0.46)**2 + (0.1/143)**2   ) for i in range(5) ]


print(m[::-1])
print(deltalDown)
print(sigmalDown)

coefsUp = np.polyfit(deltalUp, m,1)
pUp = np.poly1d(coefsUp)
coefsDown = np.polyfit(deltalDown, m[::-1],1)
pDown = np.poly1d(coefsDown)
x=[0,1]
y = [coefsUp[0]*i+coefsUp[1] for i in x]
xDown=[0,1]
yDown = [coefsDown[0]*i+coefsDown[1] for i in xDown]
fig, ax = plt.subplots()

ax.set_xlabel('$\Delta l$, мм')
ax.set_ylabel('P, Н')

ax.scatter(deltalUp, m, label='P =' + str( round(coefsUp[0], 3)) + '$\cdot \Delta l$' + '+' + str(  round(coefsUp[1],3)  ) + ' Н' )
ax.plot(x , y, c='red')


# ax.scatter(deltalDown, m[::-1], label='P =' + str( round(coefsDown[0], 3)) + '$\cdot \Delta l$' + '+' + str(  round(coefsDown[1],3)  ) + ' Н')
# ax.plot(xDown , yDown, c='red')


print(coefsUp[0], coefsUp[1])
print(coefsDown[0], coefsDown[1])
ax.set_xlim(0,1.1)
ax.set_ylim(0,17)
ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
# plt.savefig('up.jpg')


