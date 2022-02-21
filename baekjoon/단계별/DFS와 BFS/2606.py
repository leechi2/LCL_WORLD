import sys
input = sys.stdin.readline
n = int(input())
p = int(input())
graph = [[] for _ in range(n+1)]
visted = [ False for _ in range(n+1)]
for _ in range(p):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

  
def dfs(n):
  visted[n] = True
  for i in graph[n]:
    if not visted[i]:
      dfs(i)
dfs(1)  
print(visted.count(True)-1)