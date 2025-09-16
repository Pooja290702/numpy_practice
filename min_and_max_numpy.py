'''
Task

You are given a 2-D array with dimensions X.
Your task is to perform the min function over axis  and then find the max of that.

Input Format

The first line of input contains the space-separated values of  and.
The next  lines contain space-separated integers.

Output Format

Compute the min along axis  and then print the max of that result.
'''
import numpy as np
n,m=map(int,input().split())
a=np.array([input().split() for i in range(n)],int)
b=np.min(a,axis=1)
print(np.max(b))
