import sys

input = sys.stdin.readline

x1, y1= map(int, input().split())
x2, y2= map(int, input().split())
x3, y3= map(int, input().split())

min_x = min(x1,x2,x3)
min_y = min(y1,y2,y3)
max_x = max(x1,x2,x3)
max_y = max(y1,y2,y3)
print((min_x+max_x)*2 - x1-x2-x3, (min_y+max_y)*2-y1-y2-y3)