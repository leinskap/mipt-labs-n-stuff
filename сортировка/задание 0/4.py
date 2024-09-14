import numpy as np
import matplotlib.pyplot as plt
import math





fig, ax = plt.subplots()
n = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])


##bubble sort
# TimeBubble = np.array([1165.9, 5570.2, 15704.1, 33730.2, 62286.6, 103200.1, 164314.0, 279220.0, 373032.2, 490352.9])
# BestTimeBubble = np.array([1010.6, 3842.4, 12747.7, 28288.4, 56669.7, 80035.5, 147229.2, 246463.9, 352645.9, 445925.2])
# WorstTimeBubble = np.array([1660.1, 8067.4, 17660.1, 39404.1, 70741.3, 127031.4, 186657.2, 290918.8, 401817.1, 514533.3])
# ax.plot(n, TimeBubble, color='red', label='Среднее время')
# ax.plot(n, WorstTimeBubble, color='orange', linestyle='dashed', label='Худшее время')
# ax.plot(n, BestTimeBubble, color='purple', linestyle='dashdot', label='Лучшее время')


# ##slection sort
# TimeSelection = np.array([4.1, 10.6, 38.3, 119.2, 419.8, 1573.0, 6029.2, 24102.7])
# BestTimeSelection = np.array([3.1, 11.1, 34.5, 116.5, 413.7, 1525.7, 5936.4, 23350.2])
# WorstTimeSelection = np.array([1.6, 8.0, 29.8, 116.0, 421.5, 1543.7, 5924.8, 23478.0])
# ax.scatter(n, BestTimeSelection, color='purple', linewidths=1)
# lineSelection, = ax.plot(n, TimeSelection, c='purple', label='Selection Sort')
# lineBestSelection, = ax.plot(n, BestTimeSelection, c='red', label='Selection Sort Best')
# lineWorstSelection, = ax.plot(n, WorstTimeSelection, c='blue', label='Selection Sort Worst')



# ##insert sort
# ti = np.array([math.log2(x) for x in [6.8, 21.1, 78.8, 311.5, 1147.4, 4542.5, 17718.8, 71019.5]])
# ax.scatter(n,ti, color = 'orange',linewidths=1)


# heapsort
n = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
TimeHeap = np.array([1272.68, 2536.46, 3952.84, 5330.08, 6671.49, 8131.22, 9552.91, 11116.3, 12578.6, 14185.9])
BestTimeHeap = np.array([1223.87, 2457.88, 3766.75, 5254.88, 6663.14, 7919.44, 9364.85, 10864.3, 12317.5, 13708])
WorstTimeHeap = np.array([1209.24, 2446.42, 3853.85, 5225.67, 6684.74, 7975.87, 9649.79, 10954.3, 12505.8, 14036.6])
ax.plot(n, TimeHeap, color='red', label='Худшее время')
ax.plot(n, BestTimeHeap, color='orange', linestyle='dashed', label='Лучшее время')
ax.plot(n, WorstTimeHeap, color='purple', linestyle='dashdot', label='Среднее время')


# quicksort
# TimeQuick = np.array([856.4, 1710.5, 2487.9, 3609.8, 4619.5, 5417.8, 6551.8, 7663.5, 8842.6, 10156.1])
# BestTimeQuick = np.array([803.9, 1556.5, 2167.7, 3127.5, 4297.7, 4343.9, 5036.8, 6316.4, 7544.2, 8528.0])
# WorstTimeQuick = np.array([])
# ax.plot(n, TimeQuick, color='red', label='Среднее время')
# ax.plot(n, BestTimeQuick, color='orange', linestyle='dashed', label='Худшее время')
# ax.plot(n, WorstTimeQuick, color='purple', linestyle='dashdot', label='Лучшее время')


ax.set_xlabel('N')
ax.set_ylabel('t')
ax.legend()
plt.show()