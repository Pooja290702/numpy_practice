import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,7,6]]])
#nditer helps in iterating over every element in a nd array.
for i in np.nditer(a):
  print(i)
  
