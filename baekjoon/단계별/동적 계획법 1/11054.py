import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
dp1 = [1]*(n)
dp2 = [1]*(n)
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp1[i] <= dp1[j]:
            dp1[i] = int(dp1[j])+1
for i in range(n-1, -1 , -1):            
    for j in range(n-1 , i, -1):
        if a[i] > a[j] and dp2[i] <= dp2[j]:
            dp2[i] = int(dp2[j])+1    

result = [ dp1[i]+dp2[i] for i in range(n) ]

print(dp1,dp2)
print(result)
print(max(result))