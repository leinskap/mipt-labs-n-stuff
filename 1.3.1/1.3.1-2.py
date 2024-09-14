import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as st
pCu = [511.6, 1014.7, 1518, 2000.5]
pCu = [m * 9.807 * 10**(-3) for m in pCu]
yCuUp = [0.72, 1.48, 2.21, 2.97]
yCuDown = [2.97, 2.26, 1.44, 0.68]


pWood = [503.1, 1006.4, 1473.1, 1984.1]
pWood = [m * 9.807 * 10**(-3) for m in pWood]
yWoodUp = [0.61, 1.24, 1.78, 2.59]
yWoodDown = [2.59, 1.82, 1.26, 0.62]


pFe = [503.1, 1006.4, 1468.2, 1979.2]
pFe = [m * 9.807 * 10**(-3) for m in pFe]
yFeUp = [0.68, 1.31, 1.97, 2.56]
yFeDown = [2.56, 2.01, 1.3, 0.69]






fig, ax = plt.subplots()

coefsCuUp = np.polyfit(yCuUp, pCu,1)
pCuUp = np.poly1d(coefsCuUp)
# ax.scatter(yCuUp, pCu, label = 'P=' + str(round(coefsCuUp[0],3)) + '$\cdot y_{max}$' + ' + ' + str(round(coefsCuUp[1],3)))
# ax.plot(yCuUp, pCuUp(yCuUp), c='red')



coefsCuDown = np.polyfit(yCuDown, pCu[::-1],1)
pCuDown = np.poly1d(coefsCuDown)
# ax.scatter(yCuDown, pCu[::-1], label = 'P=' + str(round(coefsCuDown[0],3)) + '$\cdot y_{max}$' + ' + ' + str(round(coefsCuDown[1],3)) + ' Н')
# ax.plot(yCuDown, pCuDown(yCuDown), c='red')


#----------------------------------------------------------------------------------------------------------------------------------------------------
coefsWoodUp = np.polyfit(yWoodUp, pWood,1)
pWoodUp = np.poly1d(coefsWoodUp)
# ax.scatter(yWoodUp, pWood, label = 'P=' + str(round(coefsWoodUp[0],3)) + '$\cdot y_{max}$' + ' + ' +  str(round(coefsWoodUp[1],3)))
# ax.plot(yWoodUp, pWoodUp(yWoodUp), c='red')


coefsWoodDown = np.polyfit(yWoodDown, pWood[::-1],1)
pWoodDown = np.poly1d(coefsWoodDown)
# ax.scatter(yWoodDown, pWood[::-1], label = 'P=' + str(round(coefsWoodDown[0],3)) + '$\cdot y_{max}$' + ' + ' + str(round(coefsWoodDown[1],3)) + ' Н')
# ax.plot(yWoodDown, pWoodDown(yWoodDown), c='red')



#------------------------------------------------------------------------------------------------------------------------------------------------------------

coefsFeUp = np.polyfit(yFeUp, pFe,1)
pFeUp = np.poly1d(coefsFeUp)
# ax.scatter(yFeUp, pFe, label = 'P=' + str(round(coefsFeUp[0],3)) + '$\cdot y_{max}$' + ' ' + ' ' +  str(round(coefsFeUp[1],3)))
# ax.plot(yFeUp, pFeUp(yFeUp), c='red')


coefsFeDown = np.polyfit(yFeDown, pFe[::-1],1)
pFeDown = np.poly1d(coefsFeDown)
# ax.scatter(yFeDown, pFe[::-1], label = 'P=' + str(round(coefsFeDown[0],3)) + '$\cdot y_{max}$' + ' ' + ' ' + str(round(coefsFeDown[1],3)) + ' Н')
# ax.plot(yFeDown, pFeDown(yFeDown), c='red')



ax.legend()
plt.grid(True, which='major', color='grey', linestyle='-')
plt.grid(True, which='minor', color='#999999', linestyle='dashed', alpha=0.2)
plt.minorticks_on()
ax.set_xlabel('$y_{max}$, мм')
ax.set_ylabel('P, Н')

# plt.savefig('CuUp.jpg')
# plt.savefig('CuDown.jpg')
# plt.savefig('WoodUp.jpg')
# plt.savefig('WoodDown.jpg')
# plt.savefig('FeUp.jpg')
# plt.savefig('FeDown.jpg')
# plt.show()


k1 = coefsCuDown[0]
k2 = coefsCuUp[0]

k = (k1+k2)/2 * 1000
print(k)
E = k* 0.5**3 / (4*2.18*10**(-2)*(0.45)**3 * 10**(-6))
print(E/10**10)

k1 = coefsFeDown[0]
k2 = coefsFeUp[0]
k = (k1+k2)/2 * 1000
print(k)
E = k* 0.5**3 / (4*2.1*10**(-2)*(0.39)**3 * 10**(-6))
print(E/10**10)


k1 = coefsWoodDown[0]
k2 = coefsWoodUp[0]
k = (k1+k2)/2 * 1000
E = k* 0.5**3 / (4*2.12 *10**(-2)*(0.95)**3 * 10**(-6))
print(E/10**10)

# print(pCu)
# print(yCuUp)
# print(pCu[::-1])
# print(yCuDown)
#
# print(pWood)
# print(yWoodUp)
# print(pWood[::-1])
# print(yWoodDown)

print(pFe)
print(yFeUp)
print(pFe[::-1])
print(yFeDown)