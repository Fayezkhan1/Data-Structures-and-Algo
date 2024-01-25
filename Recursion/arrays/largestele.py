#brute force
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    a=sorted(arr)
   
    return a[-1]
    pass
#optimal code
max=arr[0]
for i in range(len(arr)):
    if max<arr[i]:
        max=arr[i]
return max