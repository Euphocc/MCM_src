import os

import pandas as pd


def number_to_str(i):
    if i < 10:
        return "0" + str(i)
    return str(i)


def csv_append(filedir):
    files = os.listdir(filedir)
    df1 = pd.read_csv(os.path.join(filedir, files[0]), header=None)
    for e in files[1:]:
        df2 = pd.read_csv(os.path.join(filedir, e), header=None)
        df1 = pd.concat((df1, df2), axis=0, join='inner')
    return df1


# df = pd.read_csv("./data/txtdata/a01/p1/s01.txt",header=None).values
for i in range(1, 20):
    df = []
    for j in range(7, 9):
        filedir = "./data/txtdata/a" + number_to_str(i) + "/p" + str(j)
        df.append(csv_append(filedir))
    action_df = pd.concat((df[0], df[1]), axis=0, join='inner')
    fileoutputname = "./data/txtdata/a" + number_to_str(i) + "/data_test.csv"
    action_df.to_csv(fileoutputname, sep=',', index=False, header=False)

data = pd.read_csv("./data/txtdata/a01/data_test.csv",header=None)
for i in range(2,20):
    df = pd.read_csv("./data/txtdata/a"+number_to_str(i)+"/data_test.csv",header=None)
    data = pd.concat((data,df),axis=0,join='inner')
    data.to_csv("./data/txtdata/data_test.csv",sep=',',index=False,header=False)