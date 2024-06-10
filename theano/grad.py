import theano

x = theano.tensor.fscalar('x')
y = 1 / (1 + theano.tensor.exp(-x))
dx = theano.grad(y, x) # 偏导数函数
f = theano.function([x], dx) # 定义函数f，输入为x，输出位s函数的偏导数
print(f(0)) # 计算当x=3的时候，函数y的偏导数，输出为0.25