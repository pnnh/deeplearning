import numpy as np

nd14 = np.arange(9).reshape([3, 3])
print(nd14)
# 矩阵转置

print("n14矩阵转置")
print(np.transpose(nd14))
# 矩阵乘法运算
a = np.arange(12).reshape([3, 4])
b = np.arange(8).reshape([4, 2])
print("a矩阵")
print(a)
print("b矩阵")
print(b)
print("a*b矩阵乘法运算")
print(a.dot(b))
# 求矩阵的迹

print("a矩阵的迹")
print(a.trace())
# 求矩阵的行列式

print("nd14矩阵的行列式")
print(np.linalg.det(nd14))
# 计算逆矩阵
c = np.random.random([3, 3])
print("c矩阵")
print(c)
d = np.linalg.solve(c, np.eye(3))
print("c矩阵的逆矩阵")
print(d)
