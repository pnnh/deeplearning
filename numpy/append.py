import numpy as np

a = np.arange(4).reshape(2,2)
b = np.arange(4).reshape(2,2)

# 按行合并
c = np.append(a, b, axis=0)
print(c)
print("合并后数据维度", c.shape)

# 按列合并
d = np.append(a, b, axis=1)
print("按列合并结果：")
print(d)
print("合并后数据维度", d.shape)
