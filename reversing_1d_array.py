import numpy as np
arr= np.array([1,2,3,4,5])
a1=np.array([6,7,8,9,0])
print(arr[::-1])
#arrays cannot be reversed, so we use slicing to reverse an array
#we can also use np.flip to reverse an array
a2=np.flip(a1)
print(a2)
