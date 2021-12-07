import sys

input = sys.stdin.readline

a = int(input())

n=1
if a == 1:
    print(1)
else:
    a -=1
    while a > 0:
        a -= n *6
        n+=1
    print(n)    