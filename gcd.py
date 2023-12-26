def calcGDC(n:int, m: int) -> int:
    
    
    while n>0 and m>0:
        if n>m:
            n=n%m
        else:
            m=m%n
    if n==0:
        return m
    else:
        return n