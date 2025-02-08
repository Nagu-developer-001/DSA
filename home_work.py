# # #HOME WORK 
# # # A
# # #BC
# # #DEF
# # #GHIJ
# # n=4
# # ch='A'
# # for i in range(n):
    # # for j in range(i+1):
        # # print(ch,end="")
        # # chrN = ord(ch)
        # # ch = chr(chrN+1)
    # # print("\n")
# # # pattern 2
# # # ch='A'
# # # for i in range(n):
    # # # for j in range(i,-1,-1):
        # # # print(ch,end="")
        # # # chrN = ord(ch)
        # # # ch = chr(chrN+j)
    # # # print("\n")
# # # A
# # # BA
# # # CBA
# # # DCBA

# # # 1111
 # # # 222
  # # # 33
   # # # 4
# # for i in range(0,n):
    # # for j in range(i):
        # # print(" ",end="")
    # # for j in range(n-i):
        # # print(i+1,end="")
    # # print("\n")
    
# n=5
# for i in range(0,n):
    # for j in range(n-i-1):
        # print(" ",end='')
    # for j in range(i+1):
        # print(j+1,end="")
    # for j in range(i,0,-1):
        # print(j,end="")
    # print("\n")

n = 4
for i in range(n):
    #to print first set of stars
    for j in range(i):
        print("*",end="")
    #print spaces
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for j in range(2*i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()