def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    count=0
    for i in range(n):
        if i%2==0:
            count=1
        else:
            count=0
    
        for j in range(i+1):
            
            print(count,end=" ")
            if count==0:
                count+=1
            else:
                count-=1
            
            
        print()

nBinaryTriangle(3)