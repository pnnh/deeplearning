import numpy as np

from numpy import random as nr

a = np.arange(1, 25, dtype=float)
c1 = nr.choice(a, size=(3, 4))  # 从a中随机选取3*4个数
print("随机可重复抽取：")
print(c1)
c2 = nr.choice(a, size=(3, 4), replace=False)  # 从a中随机选取3*4个数，不重复
print("随机不重复抽取：")
print(c2)
c3 = nr.choice(a, size=(3, 4), p=a/np.sum(a))  # 按照a中的概率分布，随机选取3*4个数
print("按概率抽取：")
print(c3)