# import math
# def F(a, b):
#     if a == b:
#         return a
#     else:
#         return (a - b) / (math.log(a) - math.log(b))
#
# a = [21954/12534.72,12534.72/2366176.91,2366176.91/10121217,10121217]
# b = [20264.52/12767.35,12767.35/1942673.98,1942673.98/10224167,10224167]
#
# w = F(21954,20264.52)
# delta = []
# for i in range(0,4):
#     delta.append(w*math.log(b[i]/a[i]))
#
# print(delta)
# print(20264.52-21954)
import numpy as np
import pandas as pd
import math
import statsmodels.api as sm
from PyLMDI import PyLMDI
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

data = pd.read_excel(r"./data/problem02_data.xlsx")
data = data.values
data = data[:, 1:8]
emission = data.copy()
for i in range(0, 5):
    for j in range(0, 6):
        emission[i, j] = emission[i, j] / emission[i, j + 1]

def F(a, b):
    if a == b:
        return a
    else:
        return (a - b) / (math.log(a) - math.log(b))


res_LMDI = emission.copy()
for i in range(1, 5):
    for j in range(0, 7):
        res_LMDI[i, j] = F(data[i, 0], data[i - 1, 0]) * math.log(emission[i, j] / emission[i - 1, j])
res_LMDI = res_LMDI[1:, :]
print(res_LMDI)