import sys
input = sys.stdin.readline

n = int(input())

base = list(map(int,input().split()))
dp = [1] * n
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        if base[i] > base[j] and dp[i] <= dp[j]:
            dp[i] = int(dp[j])+1




print(dp)