import sys
from types import resolve_bases
input = sys.stdin.readline

n = int(input())

dt = list(map(int,input().split()))
dt.sort()
result = 0

for i in range(n):
    result += (n-i) * dt[i]

print(result)