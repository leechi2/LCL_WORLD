import sys

input = sys.stdin.readline

a = int(input())

n=int(1)
temp = a
if a == 1:
    print('1/1')
else:
    while temp > n:
        temp -= n
        n += 1
        
    if n % 2 ==0:
        print(temp, end="")
        print('/', end="")
        print(n + 1 - temp)
    else:
        print(n + 1 - temp, end="")
        print('/', end="")
        print(temp)