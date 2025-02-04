# TRIANGLE PATTERN USING STARS
# *
# **
# ***
# ****
n=4
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
#TRIANGLE PATTERN USING NUMBERS
# 1
# 22
# 333
# 4444
n=4
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print("\n")
# TRIANGLE PATTERN USING ALPHABETS
# A
# BB
# CCC
# DDDD
# EEEEE
n=5
ch = 'A'
for i in range(n):
    for j in range(i+1):
        print(ch,end=" ")
        chrN = ord(ch)
    ch = chr(chrN+1)
    print("\n")