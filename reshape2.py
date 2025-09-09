import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a1=a.reshape(3,2,2)
print(a1)

#ex2
#we can replace one dimension with -1, which means we are giving an unknown dimension, so that numpy will calculate the number for us
a2=a.reshape(2,3,-1)
print(a2)
