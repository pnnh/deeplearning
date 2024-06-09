import numpy as np

a = np.arange(10)
b = np.arange(10)

print("两个shape相同的数组相加：", a + b)
print("一个数组与标量相加：", a + 3)
print("一个数组与标量相乘：", a * 3)
print("一个数组与标量相除：", a / 3)
print("两个向量相乘：", a * b)
# 多维数组之间的运算
c = np.arange(10).reshape([5, 2])
print(c)
d = np.arange(2).reshape([1, 2])
print(d)
print("多维数组相加：", c + d)  # 广播机制，首先将d数组进行复制扩充为[5, 2]的形状，然后再进行相加