n=5
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print(j+1,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print("\n")
        