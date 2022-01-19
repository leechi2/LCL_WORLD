import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
qq = deque([])
for _ in range(n):
    temp = input().split()
    if temp[0] == 'push_front':
        qq.appendleft(int(temp[1]))
    elif temp[0] == 'push_back':
        qq.append(int(temp[1]))
    elif temp[0] == 'pop_front':
        if len(qq) > 0:
            print(qq.popleft())
        else:
            print(-1)
    elif temp[0] == 'pop_back':
        if len(qq) > 0:
            print(qq.pop())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(qq))
    elif temp[0] == 'empty':
        if len(qq) > 0:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if len(qq) > 0:
            print(qq[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if len(qq) > 0:
            print(qq[-1])
        else:
            print(-1)