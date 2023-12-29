#OPTIMAL
n=int(input())
x=n
count=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        count+=1
        if n/i!=i:
            count+=1
if count==2:
    print("YES")
else:
    print("NO")

#BRUTE FORCE
# n=int(input())

# x=n-1
# if(n==1):
#     print("NO")
#     exit()
# while x>1:
#     if n%x==0:
#         print("NO")
#         exit()
#     x-=1
# print("YES")
