import sys
from collections import deque
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

for _ in range(int(input())):
    n = int(input())
    visited = [[0]*n for _ in range(n)]
    st_x, st_y = map(int, input().split())
    end_x, end_y = map(int,input().split())
    que = deque([[st_x,st_y]])
    while que:
        x,y = que.popleft()
        if x == end_x and y == end_y:
            print(visited[y][x])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if - 1 < nx < n and - 1 < ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                que.append([nx,ny])



