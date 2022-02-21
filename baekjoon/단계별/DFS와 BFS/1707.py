import sys
from collections import deque

input = sys.stdin.readline

def bfs(n):
    visited[n] = 1
    que = deque()
    que.append(n)

    while que:
        tmp = que.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = -visited[tmp]
                que.append(i)
            elif visited[i] == visited[tmp]:
                return False
    return True




for _ in range(int(input())):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    rl = True

    for i in range(1,v+1):
        if visited[i] == 0:
            if not bfs(i):
                rl = False
    print('YES' if rl else 'NO')







