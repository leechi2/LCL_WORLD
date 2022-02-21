import sys

n,m = map(int,input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int,input().split())))
    
p,k = map(int,input().split())

for i in range(p):
    b.append(list(map(int,input().split())))

r = [[0]*n for _ in range(k)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            r[i][j] += a[i][q] * b[q][j]

for i in range(n):
    for j in range(k):
        print(r[i][j],end=' ')
    print()