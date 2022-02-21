import sys
input = sys.stdin.readline

n = int(input())
dt = []

for _ in range(n):
    dt.append(list(str(input().rstrip())))
print(dt[0][0])
graph = [[[] for _ in range(n)] for _ in range(n)]
visted = [[False for _ in range(n)] for _ in range(n)]

def gm(x,y):
    if x > 0:
        if dt[x-1][y] == '1':
            graph[x][y].append((x-1,y))
    if y > 0:
        if dt[x][y-1] == '1':
            graph[x][y].append((x,y-1))
    if x < n-1:
        if dt[x+1][y] == '1':
            graph[x][y].append((x+1,y))
    if y < n-1:
        if dt[x][y+1] == '1':
            graph[x][y].append((x,y+1))

for i in range(n):
    for j in range(n):
        if dt[i][j] == '1':
            gm(i,j)



def dfs(x,y):
    global temp
    visted[x][y] = True
    temp += 1
    for i in graph[x][y]:
        if not visted[i[0]][i[1]]:
            dfs(i[0],i[1])

rl = []

for i in range(n):
    for j in range(n):
        temp = 0
        if visted[i][j] == False and dt[i][j] == '1':
            dfs(i,j)
            rl.append(temp)

print(len(rl))
for i in sorted(rl):
    print(i)

