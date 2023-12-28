def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    

    if n==0:
        return 0
    x=n
    sum=0
    for i in range(1,int(n**0.5)+1):

        if n%i==0:
            sum+=i

            if n/i!=i:
                sum+=int(n/i)
    return sum +sumOfAllDivisors(n-1)