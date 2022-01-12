import sys
input = sys.stdin.readline

n = int(input())
dt = []
for _ in range(n):
    dt.append(list(map(int,input().split())))

dt.sort(key = lambda x:x[0])

dp = [1] * (n)

for i in range(1,n):
    for j in range(i):
        if dp[i] <= dp[j] and dt[i][1] > dt[j][1]:
            dp[i] = int(dp[j]) + 1

print(n - max(dp))

