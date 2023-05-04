import numpy as np
import pandas as pd
import math


def F(a, b):
    if a == b:
        return a
    else:
        return (a - b) / (math.log(a) - math.log(b))


data = pd.read_excel(r"./data/problem02_data.xlsx")
data = data.values
data = data[:, 1:8]
emission = data.copy()
for i in range(0, 5):
    for j in range(0, 6):
        emission[i, j] = emission[i, j] / emission[i, j + 1]
res_LMDI = emission.copy()
for i in range(1, 5):
    for j in range(0, 7):
        res_LMDI[i, j] = F(data[i, 0], data[i - 1, 0]) * math.log(emission[i, j] / emission[i - 1, j])
res_LMDI = res_LMDI[1:, :]
delta_C = []
for i in range(1, 5):
    delta_C.append(data[i, 0] - data[i - 1, 0])
delta_C = np.asarray(delta_C)
weight_LMDI = res_LMDI.copy()
for i in range(0, 4):
    for j in range(0, 7):
        weight_LMDI[i, j] /= delta_C[i]

print(weight_LMDI)
print(delta_C)
