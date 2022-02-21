import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline 

def gm(y,x):
    if x > 0:
        if dt[y][x-1] == 1:
            graph[y][x].append((y,x-1))
    if y > 0:
        if dt[y-1][x] == 1:
            graph[y][x].append((y-1,x))
    if x < m-1:
        if dt[y][x+1] == 1:
            graph[y][x].append((y,x+1))
    if y < n-1:
        if dt[y+1][x] == 1:
            graph[y][x].append((y+1,x))


def dfs(y,x):
    visted[y][x] = True
    for i in graph[y][x]:
        if not visted[i[0]][i[1]]:
            dfs(i[0],i[1])

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    dt = [[0 for _ in range(m)] for _ in range(n)]
    graph = [[[] for _ in range(m)] for _ in range(n)]
    visted = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a,b = map(int,input().split())
        dt[b][a] = 1
    
    for j in range(n):
        for i in range(m):
            if dt[j][i] == 1:
                gm(j,i)


    temp = 0
    
    for j in range(n):
        for i in range(m):
            if dt[j][i] == 1 and visted[j][i] == False:
                dfs(j,i)
                temp += 1
    print(temp)