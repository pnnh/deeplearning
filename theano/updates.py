import theano

w = theano.shared(1)
x = theano.tensor.iscalar('x')
# 定义函数自变量为x，因变量为w，当函数执行完毕后，更新参数w=w+x
f = theano.function([x], w, updates=[[w, w + x]])
print(f(3)) # 输出为w
print(w.get_value()) # 这个时候可以看到w=w+x为4