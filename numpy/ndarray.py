import numpy as np


def test():
    list1 = [3.14, 2.17, 0, 1, 2]
    nd1 = np.array(list1)

    print(nd1)
    print(nd1.dtype)
    print(type(nd1))


test()

print("==================")


def test2():
    list2 = [[3.14, 2.17, 0, 1, 2], [1,2, 3, 4, 5]]
    nd2 = np.array(list2)
    print(nd2)
    print(nd2.dtype)
    print(type(nd2))


test2()

print("==================")


def test3():
    nd5 = np.random.random([3,3])
    print(nd5)
    print(type(nd5))


test3()


print("==================")


def test4():
    np.random.seed(123)
    nd5_1=np.random.randn(2, 3)
    print(nd5_1)
    np.random.shuffle(nd5_1)
    print("After shuffle:")
    print(nd5_1)
    print(type(nd5_1))


test4()