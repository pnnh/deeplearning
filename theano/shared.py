import theano
import numpy as np
import theano.tensor as T
data = np.array([[1, 2], [3, 4]])
shared_data = theano.shared(data)
print('shared_data:', shared_data.get_value())
print('shared_data type:', type(shared_data))