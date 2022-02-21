from operator import index
import sys
from collections import deque

n, k= map(int, input().split())
dt = deque([i for i in range(1,n+1)])
pr = list(map(int,input().split()))

print(dt.index(2))
count = 0
for i in pr:
    if dt.index(i) >= len(dt) - dt.index(i):
        count += int(len(dt) - dt.index(i))
        for _ in range(len(dt) - dt.index(i)):
            dt.appendleft(dt.pop())
    else:
        count += int(dt.index(i))
        for _ in range(dt.index(i)):
            dt.append(dt.popleft())
    print(dt)
    dt.popleft()
print(count)
