import sys
input = sys.stdin.readline
n,k = map(int,input().split())

dt = [[0,0]]

dp = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    dt.append(list(map(int,input().split())))

for i in range(1,n+1):
    for p in range(1,k+1):
        if p < dt[i][0]:
            dp[i][p] = int(dp[i-1][p])
        else:
            dp[i][p] = max(dp[i-1][p-dt[i][0]]+dt[i][1], dp[i-1][p])


print(dp[n][k])     





