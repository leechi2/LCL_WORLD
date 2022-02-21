import sys

input = sys.stdin.readline

n = int(input())


dp = [0,1,1,1,1,1,1,1,1,1]

if n == 1:
    print(sum(dp))
else:
    for i in range(2,n+1):
        temp = list(dp)
        for j in range(10):
            if j == 0:
                dp[j] = temp[1]
            if j == 9:
                dp[j] = temp[8]
            if 0<j<9:
                dp[j] = int(temp[j-1] + temp[j+1]) % 1000000000

print(sum(dp)%1000000000)

