import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())

dt = [list(map(int,input().split())) for _ in range(n)]
visited = [[ -1 for _ in range(m)] for _ in range(n)]

que = deque([])
for j in range(n):
    for i in range(m):
        if dt[j][i] == 1:
            que.append([i,j])
            visited[j][i] = 0
        if dt[j][i] == -1:
            visited[j][i] = 'empty'

while que:
    x,y = que.popleft()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1:
            if visited[ny][nx] == -1 and dt[ny][nx] == 0:
                que.append([nx,ny])
                visited[ny][nx] = visited[y][x] + 1

rt = 0
for j in range(n):
    for i in range(m):
        if visited[j][i] == -1:
            print(i,j)
            print(-1)
            exit(0)
        if visited[j][i] == 'empty':
            continue
        else:   
            if visited[j][i] > rt :
                rt = int(visited[j][i])
print(rt)