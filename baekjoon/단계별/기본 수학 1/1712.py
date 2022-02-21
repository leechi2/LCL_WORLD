import sys

input = sys.stdin.readline

a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

n= 1 
if b >= c:
    print(-1)
else:
    temp = c - b
    n = a // temp +1
    

    print(n)  
