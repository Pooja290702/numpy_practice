import numpy as np
a=np.array([[[1,2,3,4],[5,6,7,8]],[[9,8,7,6],[5,4,3,2]]])
for i in a:
  print(i)
#as this is a nd array, this above iteration does not print each individual element, it prints each dimension values
#to get individual elements, we have to iterate the dimensions also, as shown below
for i in a:
  for j in i:
    for k in j:
      print(k)
