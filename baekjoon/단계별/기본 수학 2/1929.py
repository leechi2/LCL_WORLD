import sys

input = sys.stdin.readline

a, b = map(int, input().split())
if a == 1:
    a = 2
for p in range(a,b+1):
    temp = 0
    for i in range(2, int((p+1)**(1/2))+1):
        if p % i ==0:
            temp = 1
            break
    if temp == 0:
        print(p)