from sklearn.preprocessing import scale
import numpy as np

n = int(input())
a = input().split(' ')
a = np.asarray(a)
res = scale(X=a)
for i in range(0,n):
    print(res[i])