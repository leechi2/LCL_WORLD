import sys

input = sys.stdin.readline
n = int(input())
data_base = []
for i in range(n):
    a,b = map(int, input().split())
    data_base.append([a,b,1])
for i in range(n):
    for j in range(n):
        if data_base[j][0] > data_base[i][0] and data_base[j][1] > data_base[i][1]:
            data_base[i][2] +=1
for i in range(n):
    print(data_base[i][2], end=' ')