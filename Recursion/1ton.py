from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    if x< 1:
        return
    else:
        # Print the current value of n
        

        # Recursive call with the next value (n-1)
        return printNos(x - 1)