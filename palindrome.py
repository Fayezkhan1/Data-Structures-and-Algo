n=int(input())  
# taking n as a input 
## write your code !!
x=n
rev=0
while x>0:
    digit=x%10
    x//=10
    rev=10*rev+digit

if rev==n:
    print("true")
else:
    print("false")
