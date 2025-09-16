import numpy as np
r=3
c=4
print(np.eye(r,c,k=0))   #k=0 means main diagonal
print(np.eye(r,c,k=1))   #k=1 means one step higher diagonal or the diagonal which starts at 1st index in 1st row
print(np.eye(r,c,k=-1))  #k=-1 means one step lower diagonal or the 1st element below the 0th position.
