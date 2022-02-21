import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
qq = deque([ i for i in range(1,n+1)])
print('<', end='')
for _ in range(n-1):
    for _ in range(k-1):
        qq.append(qq.popleft())
    print(qq.popleft(),end=', ')
print(qq[0],end='')
print('>')