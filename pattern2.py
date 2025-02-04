#pattern - 2 printing squared pattern numbers in contigious manner
n = 5
num = 1
for i in range(0,n):
    for j in range(0,n):
       print(num,end=",") 
       num+=1
    print("\n")
#pattern - 2 printing squared pattern Alphabets in contigious manner
ch = 'A'
for i in range(0,n):
    for j in range(0,n):
        print(ch,end=",")
        chrNum = ord(ch)
        ch = chr(chrNum+1)
    print("\n")