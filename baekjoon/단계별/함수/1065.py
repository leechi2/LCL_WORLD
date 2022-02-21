import sys
from collections import defaultdict

input= sys.stdin.readline

def sol(x : int) -> int:
    nnn = x //100
    nn = (x-100*nnn)//10
    n = x % 10
    if nn == (n+nnn)/2:
        return x
    


n = int(input())
temp = 0

list = [x for x in range(1,100)]

if n < 100:
    print(n)
else:
    for i in range(100,n+1):
        temp = sol(i)
        if type(temp) == int:
            list.append(temp)
    print(len(list))




    
