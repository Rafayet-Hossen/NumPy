#you can create n dim array in python

import numpy as np

arn = np.array([1, 2, 3], ndmin = 10) #this will create 10 D array

print(arn)
print(arn.ndim)
print(arn.shape)

'''
output is:

    [[[[[[[[[[1 2 3]]]]]]]]]]
    10
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 3)

'''