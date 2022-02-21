import sys

input = sys.stdin.readline

n = int(input())

color = []

for i in range(n):
    color.append(list(map(int,input().split())))

for i in range(1,n):
    color[i][0] += min(color[i-1][1], color[i-1][2])
    color[i][1] += min(color[i-1][0], color[i-1][2])
    color[i][2] += min(color[i-1][1], color[i-1][0])

print(min(color[n-1]))