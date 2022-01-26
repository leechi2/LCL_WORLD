import sys
n = int(input())
dt = [list(input()) for _ in range(n)]
rl = []
def jg(n,x,y):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if dt[x][y] != dt[i][j]:
                rl.append('(')
                jg(n//2,x,y)
                jg(n//2,x,y+n//2)
                jg(n//2,x+n//2,y)
                jg(n//2,x+n//2,y+n//2)
                rl.append(')')
                return
    rl.append(dt[x][y])
jg(n,0,0)
print(''.join(rl))
            
