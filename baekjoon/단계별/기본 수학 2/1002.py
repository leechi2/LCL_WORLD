import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2,y2, r2 = map(int, input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if d > r1+r2:
        print(0)
    elif d == 0 and r1 ==r2:
        print(-1)
    elif d == r1+r2:
        print(1)
    elif abs(r1-r2)< d < r1+r2:
        print(2)
    elif abs(r1-r2)== d:
        print(1)
    else:
        print(0)
