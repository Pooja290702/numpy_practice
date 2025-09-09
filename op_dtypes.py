import numpy as np
a=np.array([1,2,3,4])
for x in np.nditer(a, flags=['buffered'],op_dtypes=['S']):
  print(x)
  '''in the above code,
  i forced the iteration to print the array in different data type, 
  so output would be in string format instead of int
  '''
