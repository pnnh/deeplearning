import numpy as np

nd15=np.arange(6).reshape(2, -1)
print(nd15)
print("按照列优先展平", nd15.ravel('F'))
print("按照行优先展平", nd15.ravel())