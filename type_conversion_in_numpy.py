
import numpy as np
#type1 converting float into int
arr=np.array([1.2,2.3,3.4,4.5,5.6])
newarr=arr.astype('i')
print(newarr.dtype)
#type2
a2=arr.astype(int)
a3=arr.astype(bool)
print(a2,a3)
