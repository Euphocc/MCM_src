import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/txtdata/data.csv', header=None)
print(np.any(data.isnull()))


data = data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
res = data.var()
xdata = range(1,46)
for i in range(len(xdata)):
    plt.bar(xdata[i],res[i])
plt.title("The variance of the feature")
plt.show()

#
# corr = data.corr()
# cols_str = 'T_xacc1,T_yacc1,T_zacc1,T_xacc2,T_yacc2,T_zacc2,T_xacc3,T_yacc3,T_zacc3,RA_xgyro1,RA_ymag1,RA_zmag1,RA_xgyro2,RA_ymag2,RA_zmag2,RA_xgyro3,RA_ymag3,RA_zmag3,LA_xgyro1,LA_ymag1,LA_zmag1,LA_xgyro2,LA_ymag2,LA_zmag2,LA_xgyro3,LA_ymag3,LA_zmag3,RL_xgyro1,RL_ymag1,RL_zmag1,RL_xgyro2,RL_ymag2,RL_zmag2,RL_xgyro3,RL_ymag3,RL_zmag3,LL_xgyro1,LL_ymag1,LL_zmag1,LL_xgyro2,LL_ymag2,LL_zmag2,LL_xgyro3,LL_ymag3,LL_zmag3'
# cols = cols_str.split(',')
# corr.columns = cols
# corr.index = cols