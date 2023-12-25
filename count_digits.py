def countDigits(n: int) -> int:
    count=0
    stringify=str(n)
    
    for i in stringify:
        if int(i)==0:
            continue
        if n%int(i)==0:
            count+=1
    return count

countDigits(35)