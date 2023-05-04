import numpy as np
import matplotlib.pyplot as plt


def grouped_avg(myArray, N=2):
    result = np.cumsum(myArray, 0)[N - 1::N] / float(N)
    result[1:] = result[1:] - result[:-1]
    return result


def grouped_var(original_array, N):
    newList = []
    for i in range(0, original_array.shape[0], N):
        r = original_array[i:i + N, :].var(axis=0)
        newList.append(r)
    new_array = np.asarray(newList)
    return new_array


X_train = (np.load("./data/data_selected.npy"))[:, :]
labels = []
for i in range(1, 20):
    for j in range(0, 360):
        labels.append(i)
labels = np.asarray(labels)
X_test = (np.load("./data/data_test_selected.npy"))[:, :]
print(X_train.shape)
print(X_test.shape)

print(labels.shape)

X_train1 = grouped_avg(X_train, N=125)
X_train2 = grouped_var(X_train, N=125)
X_train = np.hstack((X_train1, X_train2))
print(X_train.shape)

# from sklearn import svm
# from sklearn.svm import SVC
#
# clf = svm.SVC(kernel='linear', C=20, gamma='auto',probability=True)
# # clf = svm.LinearSVC()
# clf.fit(X_train, labels)
#
# print("training score:", clf.score(X_train, labels))

X_test1 = grouped_avg(X_test, N=125)
print(X_test1.shape)
X_test2 = grouped_var(X_test, N=125)
X_test = np.hstack((X_test1, X_test2))
print(X_test.shape)
