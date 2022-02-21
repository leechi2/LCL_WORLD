import sys
from collections import deque

input = sys.stdin.readline

n,m,stt = map(int,input().split())

graph = [[] for _ in range(n+1) ]
visted = [ False for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    print(n,end=' ')
    visted[n] = True
    for i in graph[n]:
        if not visted[i]:
            dfs(i)

def bfs(n):
    visted[n] = True
    qq = deque([n])
    while qq:
        v = qq.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visted[i]:
                qq.append(i)
                visted[i] = True
dfs(stt)
print()
visted = [ False for _ in range(n+1)]
bfs(stt)

