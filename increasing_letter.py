def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    a=65
    for i in range(n):
        for j in range(i+1):
            print(chr(j+65),end=" ")
        print()