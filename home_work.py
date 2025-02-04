#HOME WORK 
# A
#BC
#DEF
#GHIJ
n=4
ch='A'
for i in range(n):
    for j in range(i+1):
        print(ch,end="")
        chrN = ord(ch)
        ch = chr(chrN+1)
    print(" ")
# pattern 2
# ch='A'
# for i in range(n):
    # for j in range(i,-1,-1):
        # print(ch,end="")
        # chrN = ord(ch)
        # ch = chr(chrN+j)
    # print("\n")
# A
# BA
# CBA
# DCBA

# 1111
 # 222
  # 33
   # 4
for i in range(0,n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print(i+1,end="")
    print("\n")