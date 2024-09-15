import numpy as np
import matplotlib as plt
# np.random.seed(seed=1234)

# Scalar
import self as self

x = np.array(6)
print ("x: ", x)
print ("x ndim: ", x.ndim) # number of dimensions
print ("x shape:", x.shape) # dimensions
print ("x size: ", x.size) # size of elements
print ("x dtype: ", x.dtype) # data type
print ("x dtype: ", x.__ge__(1)) # ????
print ("x dtype: ", x.__eq__(self,3)) # ????


