import numpy as np

np.random.seed(2018)
nd11 = np.random.random([10])
print(nd11)
print(nd11[3])
print(nd11[3:8])
print(nd11[1:6:2])  # 截取固定间隔数据
print(nd11[::-2])  # 反向截取数据
nd12=np.arange(25).reshape([5, 5])
print(nd12)
print(nd12[1:3, 1:3])   # 截取多维数组的一个区域内数据，这里是第一行到第三行，第一列到第三列的数据，不包含第三行和第三列
print(nd12[(nd12>3) & (nd12<10)])  # 截取一个多维数组中，数值在一个值域之内的数据
print(nd12[[1, 2]]) # 截取多维数组中，指定的行
print(nd12[:, 1:3])  # 截取多维数组中，指定的列

