import sys 

n = int(sys.stdin.readline())
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d' %(i+1, x,y,x+y))