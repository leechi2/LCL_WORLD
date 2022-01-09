import sys
input = sys.stdin.readline

n = int(input())
base = [0]
for _ in range(n):
    base.append(int(input()))

result = [0] * (n+2)
result[1] = int(base[1])

if n > 1:
    result[2] = int(base[1]+base[2])
if n > 2:
    result[3] = max(max(base[1],base[2]) + int(base[2]),result[2] )
if n > 3:
    for i in range(3,n):
        result[i] = max(result[i-1], base[i]+result[i-2], base[i]+base[i-1]+result[i-3])

print(result[n-1])