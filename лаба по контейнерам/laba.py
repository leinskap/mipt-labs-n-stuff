import matplotlib.pyplot as plt
import numpy as np
import math
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})
import array
## --------------------------------------------------------------------------------------------------------------------0
# with open('data.txt', 'r') as data:
#     elementNumber = []
#     y = []
#     z = []
#     for line in data:
#         p = line.split()
#         elementNumber.append(int(p[0]))
#         y.append(int(p[1]))
#         z.append(int(p[2]))
# fig, ax = plt.subplots()
# ax.plot(elementNumber, y, label='size')
# ax.plot(elementNumber, z, label='capacity')
# ax.set_xlabel('Номер итерации')
# ax.set_ylabel('Количество элементов')
# ax.legend()
# plt.minorticks_on()
# plt.savefig('(0)vector_size_capacity.png')

## ------------------------------------------------------------------------------------------------------------------1-1
# with open('data1-1.txt', 'r') as data:
#     x = []
#     y = []
#     for line in data:
#         p = line.split()
#         x.append(int(p[0]))
#         y.append(float(p[1]))
# fig, ax = plt.subplots()
# ax.plot(x, y, label='vector')
# # ax.plot(z, w, label='subvector')
# ax.set_xlabel('Номер итерации')
# a = array.array('i', (i for i in range(int(math.log(x[0], 2)) + 1, int(math.log(x[-1], 2))+1)))
# p = [math.pow(2, i) for i in a]
# u = [0*i for i in p]
# ax.scatter(p, u, color = 'red')
# ax.set_ylabel('Время')
# plt.savefig('(1-1)vector_insert_time.png')
# plt.show()

## ------------------------------------------------------------------------------------------------------------------1-2
# with open('data1-2.txt', 'r') as data:
#     z = []
#     w = []
#     for line in data:
#         p = line.split()
#         z.append(int(p[0]))
#         w.append(float(p[1]))
# fig, ax = plt.subplots()
# ax.plot(z, w)
# ax.set_xlabel('Номер итерации')
# ax.set_ylabel('Время')
# plt.savefig('(1-2)subvector_insert_time.png')
# plt.show()




## ------------------------------------------------------------------------------------------------------------------2-1
with open('data2-1.txt', 'r') as data:
    z = []
    w = []
    for line in data:
        p = line.split()
        z.append(int(p[0]))
        w.append(float(p[1]))
fig, ax = plt.subplots()
ax.plot(z, w)
ax.set_xlabel('')
ax.set_ylabel('')
ax.legend()
plt.show()
# plt.savefig('2.png')
#
#
# with open('data2-2.txt', 'r') as data:
#     z = []
#     w = []
#     for line in data:
#         p = line.split()
#         z.append(int(p[0]))
#         w.append(float(p[1]))
# fig, ax = plt.subplots()
# ax.plot(z, w)
# ax.set_xlabel('')
# ax.set_ylabel('')
# # plt.minorticks_on()
# plt.savefig('2-2.png')
#
#
# with open('data3.txt', 'r') as data:
#     z = []
#     w = []
#     for line in data:
#         p = line.split()
#         z.append(int(p[0]))
#         w.append(float(p[1]))
# fig, ax = plt.subplots()
# ax.plot(z, w)
# ax.set_xlabel('')
# ax.set_ylabel('')
# # plt.minorticks_on()
# plt.savefig('2-2.png')
# plt.show()