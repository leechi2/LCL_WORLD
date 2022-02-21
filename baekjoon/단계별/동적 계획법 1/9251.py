import sys
input = sys.stdin.readline 

a = list(str(input().rstrip()))
b = list(str(input().rstrip()))

rl = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if b[j-1] == a[i-1]:
            rl[i][j] = int(int(rl[i-1][j-1]) + 1)
        else:
            rl[i][j] = int(max(int(rl[i][j-1]),int(rl[i-1][j])))




print(rl[len(a)][len(b)])