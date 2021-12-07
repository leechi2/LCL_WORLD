import sys

input = sys.stdin.readline

i = int(input())
for _ in range(i):
    a,b = map(int, input().split())
    n = abs(a-b)
    p = int(n**(1/2))
    print((n-p**2+p-1)//p+2*p-1)