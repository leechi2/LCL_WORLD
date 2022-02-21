import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

qq = deque([i for i in range(1,n+1)])

while len(qq) > 1:
    qq.popleft()
    qq.append(qq.popleft())

print(qq)