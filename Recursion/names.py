from  typing import *

def printNtimes(n: int) -> List[str]:
    arr=[]
    if n==1:
        return ["Coding"]
    else:
        arr.append("Coding")
        return arr+printNtimes(n-1)