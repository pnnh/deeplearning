import numpy as np


def test():
    nd6 = np.zeros([3, 3])
    nd7 = np.ones([3, 3])
    nd8 = np.eye(3)
    print(nd8)
    print(np.diag([1, 2, 3]))


test()


print("==================")


def arange():
    print(np.arange(10))
    print(np.arange(0, 10))
    print(np.arange(1, 4, 0.5))
    print(np.arange(9, -1, -1))


arange()


print("==================")


def test2():
    nd9 = np.random.random([5, 5])
    print(nd9)
    np.savetxt(X=nd9, fname="./test.txt", fmt="%.2f", delimiter=",")
    nd10 = np.loadtxt("./test.txt", delimiter=",")
    print(nd10)


test2()