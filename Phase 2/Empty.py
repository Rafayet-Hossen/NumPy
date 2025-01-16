import numpy as np

ar_emp = np.empty((2,2))

print(ar_emp) #here you will find random values or previous array values
print(f'Array is {ar_emp.shape}') #row and col in 2d array
print(f'Array is: {ar_emp.ndim} D') #dimention of the array
print(f'Array size: {ar_emp.size}') #size of the array
print(f'Array dtype: {ar_emp.dtype}') #tupe of the array
print(f'Array element size: {ar_emp.itemsize}') # size of each item