import numpy as np

arr_ones = np.ones((2,3),int)
print(arr_ones)
print(f'Array is {arr_ones.shape}') #row and col in 2d array
print(f'Array is: {arr_ones.ndim} D') #dimention of the array
print(f'Array size: {arr_ones.size}') #size of the array
print(f'Array dtype: {arr_ones.dtype}') #tupe of the array
print(f'Array element size: {arr_ones.itemsize}') # size of each item