import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
from scipy.stats import trim_mean
from scipy.stats import iqr
import seaborn as sns
x = np.linspace(-3, 3, 50)
h=2
df = pd.DataFrame({'k/x': 0.03/x, 'gaussian': 1/(2*3.14)**0.5 * 2.7**(-x**2/2), 'gaussian2': 1/(2*3.14)**0.5 * 2.7**(-(x/h)**2/2)})
df.plot()
plt.show()