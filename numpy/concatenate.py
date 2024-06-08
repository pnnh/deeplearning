import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)
c = np.append(a, b)
print(c)
d = np.concatenate([a, b])
print(d)