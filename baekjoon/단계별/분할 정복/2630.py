import sys

n = int(input())
dt = [list(map(int,input().split())) for _ in range(n)]

rl = [0,0]
def jd(n, x, y):

    if n > 1:
        for i in range(x,x+n):
            for j in range(y,y+n):
                if dt[x][y]  != dt[i][j]:
                    jg = False
                    jd(n//2, int(x), y)
                    jd(n//2, x+n//2, y)
                    jd(n//2, x, y+n//2)
                    jd(n//2, x+n//2, y+n//2)
                    return
                else:
                    continue

    if dt[x][y]  == 1:
        rl[1] += 1
    else:
        rl[0] += 1


jd(n,int(0),int(0))
print(rl[0])
print(rl[1])