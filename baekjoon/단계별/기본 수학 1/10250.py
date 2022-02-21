import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    print((n-1)%h+1, end="")
    if (n-1)//h+1 < 10:
        print(0, end="")
        print((n-1)//h+1)
    else:
        print((n-1)//h+1)