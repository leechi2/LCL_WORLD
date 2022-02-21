import sys
input = sys.stdin.readline

n = int(input())
ct = list(map(int,input().split()))
co = list(map(int,input().split()))
temp = co[0]
for i in range(1,n-1):
    if co[i] < temp:
        temp = int(co[i])
    else:
        co[i] = int(temp)

re = 0
for i in range(n-1):
    re += co[i] * ct[i]

print(re)