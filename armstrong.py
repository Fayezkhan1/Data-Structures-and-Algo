
def armstrongNumber (self, n):
    # code here 
    x=n
    y=n
    count=0
    while x>0:
        count+=1
        x//=10
    sum=0
    while y>0:
        digit=y%10
        sum+=digit**count
        y//=10
    if sum==n:
        return True
    else:
        False
        