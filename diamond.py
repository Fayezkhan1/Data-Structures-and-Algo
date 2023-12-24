for i in range(3):
    for j in range(2-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")

    print()




for i in range(3):

    for j in range(i):
        print(" ", end="")
    for j in range(3-i):
        print("*", end="")
    for j in range(3-i-1):
        print("*", end="")
    print()