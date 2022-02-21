import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
dt = []
for _ in range(n):
    tmp = list(str(input().rstrip()))
    for i in range(m):
        tmp[i] = [int(tmp[i]),0,0]
    dt.append(tmp)
dt[0][0][1] = 1

que = deque([[0,0,0]])
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while que:
    x,y,a = que.popleft()
    if x ==m-1 and y == n-1:
        print(dt[y][x][a+1])
        exit(0)
    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= m-1 and  0 <= ny <= n-1:

            if a == 0 and dt[ny][nx][0] == 1: #벽을만났는데 뚫을수있다
                dt[ny][nx][2] = dt[y][x][1] + 1
                que.append([nx,ny,1])
            elif dt[ny][nx][a+1] == 0 and dt[ny][nx][0] == 0: # 벽아니다
                dt[ny][nx][a+1] = dt[y][x][a+1] + 1
                que.append([nx,ny,a])

print(-1)
