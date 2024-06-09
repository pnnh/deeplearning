import time
import math
import numpy as np

x = [i*0.001 for i in np.arange(1000000)]
start = time.process_time()

for i, t in enumerate(x):
    x[i] = math.sin(t)

print("math.sin: ", time.process_time() - start)

x = [i * 0.001 for i in np.arange(1000000)]
x = np.array(x)

start = time.process_time()
np.sin(x)

print("numpy.sin: ", time.process_time() - start)