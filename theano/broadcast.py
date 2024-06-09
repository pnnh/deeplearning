import theano
import numpy as np
import theano.tensor as T

r = T.row()
print('r.broadcastable:', r.broadcastable)
# (True, False)
mtr=T.matrix()
print('mtr.broadcastable:', mtr.broadcastable)
# (False, False)
f_row=theano.function([r,mtr],[r+mtr])
R=np.arange(1, 3).reshape(1, 2)
print('R:', R)
#array([[1, 2]])
M=np.arange(1, 7).reshape(3, 2)
print('M:', M)
#array([[1, 2],
#       [3, 4],
#       [5, 6]])
print('f_row(R, M):', f_row(R, M))
#array([[2, 4],
#       [4, 6],
#       [6, 8]])
