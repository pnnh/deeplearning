import theano

x, y = theano.tensor.fscalars('x', 'y')
print('x:', type(x))
z1 = x + y
print('z1:', type(z1))
z2 = x * y
print('z2:', type(z2))

# 定义x、y为自变量，z1、z2为因变量的函数
f = theano.function([x, y], [z1, z2])
# 返回当x=2.0，y=3.0时，函数f的因变量z1、z2的值
print(f(2.0, 3.0))