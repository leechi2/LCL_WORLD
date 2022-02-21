import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
dt = [0] * 100001
que = deque([n])
dt[n] = 1
while que:
    tmp = que.popleft()
    if tmp == k:
        print(dt[tmp]-1)
        exit(0)

    if tmp > 0 and dt[tmp-1] == 0:
        que.append(tmp-1)
        dt[tmp-1] = dt[tmp] + 1
    if tmp < 100000 and dt[tmp+1] == 0:
        que.append(tmp+1)
        dt[tmp+1] = dt[tmp] + 1
    if tmp < 50001 and dt[2*tmp] == 0:
        que.append(2*tmp)
        dt[2*tmp] = dt[tmp] + 1




