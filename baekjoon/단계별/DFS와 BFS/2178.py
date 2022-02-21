from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dt = [ list(map(str,input().rstrip())) for _ in range(n)]
graph = [[[] for _ in range(m)] for _ in range(n)]
visted = [[0 for _ in range(m)] for _ in range(n)]

def gm(y,x):
    if x > 0:
        if dt[y][x-1] == '1':
            graph[y][x].append([y,x-1])
    if y > 0:
        if dt[y-1][x] == '1':
            graph[y][x].append([y-1,x])
    if x < m-1:
        if dt[y][x+1] == '1':
            graph[y][x].append([y,x+1])
    if y < n-1:
        if dt[y+1][x] == '1':
            graph[y][x].append([y+1,x])

for j in range(n):
    for i in range(m):
        if dt[j][i] == '1':
            gm(j,i)
visted[0][0] = 1
queue = deque([[0,0]])
while queue:
    x,y = queue.popleft()
    if x == m-1 and y == n-1:
        print(visted[y][x])
        break

    for i in graph[y][x]:

        if visted[i[0]][i[1]] == 0 and dt[i[0]][i[1]] == '1':
            visted[i[0]][i[1]] = visted[y][x] + 1
            queue.append([i[1],i[0]])





