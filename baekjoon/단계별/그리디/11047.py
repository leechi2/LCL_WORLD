import sys
input = sys.stdin.readline 

n,k = map(int, input().split())
dt = []
for _ in range(n):
    dt.append(int(input()))
dt.reverse()
count = 0
for i in dt:
    if k // i > 0:
        count += k // i
        k -= int(k//i) * i
    else:
        continue
    print(count, k )
print(count)