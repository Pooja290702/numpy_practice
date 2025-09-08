#it helps in reshaping a 1d arrray into nd array, helps in adding or removing or changing the dimensions
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,0,11,12])
a1=arr.reshape(4,3)
a2=a1.reshape(6,2)
print(a1)
print(a2)
