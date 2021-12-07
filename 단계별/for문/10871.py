import sys
input = sys.stdin.readline
x,y = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i< y:
        print(i, end=' ')