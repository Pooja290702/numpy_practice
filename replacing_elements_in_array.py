'''Replace all numbers divisible by 5 with -1
(do this without any loop).
Print the resulting array.'''
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr[arr%5==0]=-1
print(arr)
