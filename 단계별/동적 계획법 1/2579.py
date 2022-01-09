import sys

input = sys.stdin.readline

n = int(input())
data_base = []
for _ in range(n):
    data_base.append(int(input()))

dp = [0] * len(data_base)

dp[0] = int(data_base[0])
if n > 1:
    dp[1] = data_base[0]+data_base[1]
if n > 2:
    dp[2] = max(dp[0]+data_base[2], data_base[1]+data_base[2])
if n > 3:
    for i in range(3,len(data_base)):
        dp[i] = max(dp[i-2]+data_base[i], dp[i-3]+data_base[i-1]+data_base[i])
print(dp[-1])





