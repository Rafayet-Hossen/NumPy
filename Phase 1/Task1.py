import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)
arr2 = np.array([[7 , 8, 9], [4 , 5 ,6], [1 , 2 , 3]])
print(arr2)

ans = arr1 + arr2
print("Ans array will be: ")
for i in range(0,3):
    for j in range(0,3):
        print(ans[i][j],end=" ")
    print()
