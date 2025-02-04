# TRIANGLE PATTERN  - 
# 1
# 12
# 123
# 1234
n = 4
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print("\n")
# REVERSE TRIANGLE PATTERN
# 1
# 21
# 321
# 4321
n=4
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end="")
    print("\n")
#FLOYD'S TRIANGLE PATTERN
# 1
# 23
# 456
# 78910
n=4
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end="")
        num+=1
    print("\n")
