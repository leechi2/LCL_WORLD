import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().split())

dt = []


que = deque([])
for k in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for i in range(m):
            if tmp[j][i] == 1:
                que.append([i,j,k])
    dt.append(tmp)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while que:
    x,y,z = que.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1 and 0 <= nz <= h-1 and dt[nz][ny][nx] == 0:
            que.append([nx,ny,nz])
            dt[nz][ny][nx] = dt[z][y][x] + 1

rt = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if dt[k][j][i] == 0:
                print(-1)
                exit(0)

            if dt[k][j][i]-1 > rt-1 :
                rt = int(dt[k][j][i]-1)
print(rt)