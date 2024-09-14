import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as st



# --------------------------------------------------------------------------------ИЗМЕРЕНИЕ ОБЪЁМА ВЫСОКОВАКУУМНОЙ ЧАСТИ
# высота столба масла в первом колене (см)
h1 = 38.3
sigma_h1 = 0.1
# высота столба масла во втором колене (см)
h2 = 11.8
sigma_h2 = 0.1
# разность высот (см)
delta_h = abs(h1-h2)
sigma_delta_h = delta_h * math.sqrt((sigma_h2/h2)**2 + (sigma_h1/h1)**2)
print('delta h =', delta_h, u"\u00B1", round(sigma_delta_h, 1), 'см')

# объём запертой части (см^3)
V_zap = 50
sigma_V_zap = 1
# атмосферное давление (кПа)
P_atm = 100.35
sigma_P_atm = 0.3
# плотность масла (кг/м^3)
rho_oil = 885
# ускорение свободного падения
g = 9.8154
V_fv = P_atm*1000*V_zap/(delta_h*0.01*rho_oil*g)
sigma_V_fv = V_fv * math.sqrt((sigma_P_atm/P_atm)**2 + (sigma_delta_h/delta_h)**2 + (sigma_V_zap/V_zap)**2)
print('V_fv =', round(V_fv, 1), u"\u00B1", round(sigma_V_fv, 0), 'см^3')


# высота столба масла в первом колене (см)
h3 = 33.8
sigma_h3 = 0.1
# высота столба масла во втором колене (см)
h4 = 16.7
sigma_h4 = 0.1
# разность высот (см)
delta_h = abs(h3-h4)
sigma_delta_h = delta_h * math.sqrt((sigma_h3/h3)**2 + (sigma_h4/h4)**2)
print('delta h =', round(delta_h, 1), u"\u00B1", round(sigma_delta_h, 1), 'см')


V_vv = P_atm*1000*V_zap/(delta_h*0.01*rho_oil*g) - V_fv
sigma_V_vv = V_vv * math.sqrt((sigma_P_atm/P_atm)**2 + (sigma_delta_h/delta_h)**2 + (sigma_V_zap/V_zap)**2 + (sigma_V_fv/V_fv)**2)
print('V_vv =', round(V_vv, 1), u"\u00B1", round(sigma_V_vv, 0), 'см^3')

# ---------------------------------------------------------------ПОЛУЧЕНИЕ ВЫСОКОГО ВАКУУМА И ИЗМЕРЕНИЕ СКОРОСТИ ОТКАЧКИ
# предельное давление (торр)
P_lim = 5.2 * 10**(-5)
sigma_P_lim = 0.05 * 10**(-4)
# улучшение вакуума
i = 0  # cчётчик
files = ['улучшение 1.png', 'улучшение 2.png']
data = [np.array([(5.8, 0), (5, 1), (4.3, 2.2), (3.6, 3.2), (3.0, 4.2), (2.7, 4.4), (2.1, 6.2), (1.7, 7.4),
                  (1.4, 9.2), (1.1, 11), (0.88, 13.2), (0.78, 15), (0.68, 17.2), (0.57, 23.2), (0.54, 28.2)]),
        np.array([(5.3, 0), (5.6, 1.2), (4.3, 2.1), (3.6, 3.1), (3.0, 4.1), (2.7, 4.22), (2.1, 6.1), (1.7, 7.2),
                  (1.4, 9.1), (1.1, 10.2), (0.88, 13.1), (0.78, 14.2), (0.68, 17.1), (0.57, 23.1), (0.54, 28.1)])]
for d in data:
    fig, ax = plt.subplots(figsize=(8, 5))
    pr = [x[0] - P_lim*10**4 for x in d]
    t = np.array([x[1] for x in d])
    ln_p = np.array([math.log(x) for x in pr])
    ax.scatter(t, ln_p, color='black')
    coefs = np.polyfit(t, ln_p, 1)
    p = np.poly1d(coefs)
    k = coefs[0]
    sigma_k = 1 / math.sqrt(len(pr)) * math.sqrt((st.mean(ln_p ** 2) - (st.mean(ln_p)) ** 2)/(st.mean(t ** 2) - (st.mean(t)) ** 2) - k ** 2)
    ax.plot(t, p(t), label='k = ' + str(round(k, 2)) + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{1}{c}$', color='0.9', linestyle=':')
    W = -k * V_vv
    sigma_W = W * math.sqrt((sigma_k/k)**2 + (sigma_V_vv/V_vv)**2)
    print('W = ', round(W, 1), u"\u00B1", round(sigma_W, 0), 'см^3/с')


    ax.set_ylabel('$ln(p-p_{кр})$')
    ax.set_xlabel('Время t, c')
    # ax.set_title('Зависимость ')
    ax.legend()
    plt.grid(True, which='major', color='0.8', linestyle='-')
    plt.grid(True, which='minor', color='0.85', linestyle='dashed', alpha=0.2)
    plt.minorticks_on()
    plt.savefig(files[i])
    i += 1

# ухудшение вакуума
data = [[(0.52, 0), (0.56, 1.2), (0.58, 1.4), (0.64, 3.2), (0.72, 4.37), (0.79, 6.2), (1, 10.4),
         (1.2, 14.2), (1.3, 16.2), (1.4, 18.2), (1.6, 22.4), (1.9, 28.4), (2.3, 37.2),
         (2.6, 43.15), (3, 51.4), (3.5, 62.2), (4, 73.2), (4.5, 84.4), (5, 96.15)],
        [(0.53, 0), (0.56, 1.2), (0.59, 2.2), (0.63, 3.2), (0.69, 5), (0.76, 6.2), (0.95, 10.4),
         (1.2, 16), (1.3, 18.3), (1.4, 20.2), (1.6, 25.2), (1.9, 32.2), (2.3, 42),
         (2.6, 49), (3, 58), (3.5, 70), (4, 81.2), (4.5, 93), (5, 104)]]
files = ['ухудшение 1.png', 'ухудшение 2.png']
i = 0
for d in data:
    fig, ax = plt.subplots(figsize=(8, 5))
    p = np.array([x[0] for x in d])
    t = np.array([x[1] for x in d])
    ax.scatter(t, p, color='black')
    coefs = np.polyfit(t, p, 1)
    pr = np.poly1d(coefs)
    k = coefs[0]
    sigma_k = 1 / math.sqrt(len(p)) * math.sqrt((st.mean(p ** 2) - (st.mean(p)) ** 2)/(st.mean(t ** 2) - (st.mean(t)) ** 2) - k ** 2)
    ax.plot(t, pr(t), label='k = ' + str(round(k, 2)) + u"\u00B1" + ' ' + str(round(sigma_k, 2)) + ' $\\frac{Па}{c}$', color='0.9', linestyle=':')
    Q_n = P_lim * W - k * 10**(-4) * V_vv
    sigma_Q_n = Q_n * math.sqrt((sigma_P_lim/P_lim)**2 + (sigma_W/W)**2 + (sigma_k/k)**2 + (sigma_V_vv/V_vv)**2)
    print('Q_n = ', round(Q_n * 10**4, 1), u"\u00B1", round(sigma_Q_n*10**4, 0), '* 10^4 торр * см^3/с')
    ax.set_ylabel('P')
    ax.set_xlabel('Время t, c')
    # ax.set_title('Зависимость ')
    ax.legend()
    plt.grid(True, which='major', color='0.8', linestyle='-')
    plt.grid(True, which='minor', color='0.85', linestyle='dashed', alpha=0.2)
    plt.minorticks_on()
    plt.savefig(files[i])
    i += 1


# установившееся давление, мм. рт. ст.
P_ust = 1.2 * 10**(-4)
sigma_P_ust = 0.05
# давление со стороны форвакуумной части капилляра, мм. рт. ст.
P_fv = 3.6 * 10**(-4)
sigma_P_fv = 0.05
# длина трубки, м
L = 10.8 * 10**(-2)
sigma_L = 0.05 * 10**(-2)
# радиус трубки, м
r = 0.4 * 10**(-3)
sigma_r = 0.05 * 10**(-3)
# температура, К
T = 273 + 22.6
sigma_T = 0.4
# Молярная масса, кг/моль
M = 28.97 * 10**(-3)
C_tr = 4/3 * r**3 / L * math.sqrt(2*math.pi*8.31*T/M)
epsilon_C_tr = math.sqrt(3*(sigma_r/r)**2 + (sigma_L/L)**2 + 1/4 * (sigma_T/T)**2)
print('C_tr = ', round(C_tr*10**9, 7), u"\u00B1", round(epsilon_C_tr*C_tr*10**9, 7))
W = P_fv/(P_ust-P_lim) * 4/3 * r**3 / L * math.sqrt(2*math.pi*8.31*T/M)
print('W = ', round(W*10**8, 7), u"\u00B1", round(epsilon_C_tr*W*10**8, 7))


plt.show()



