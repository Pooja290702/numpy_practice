import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array(['apple', 'banana', 'cherry'])   # this data type is <u6 because, u means unicode STRING TYPE and 6 is the maximum length of the string
arr3 = np.array([1, 2, 3, 4], dtype='S')          # s means string type but only ascii , not fully unicode. if it says s1, then only 1 char. if we print it, we get b'' bcz it indicates ascii.
arr4 = np.array([1, 2, 3, 4], dtype='i4')

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
