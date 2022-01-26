import sys
input = sys.stdin.readline

n = int(input())

def cal(a,b):
    rl = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                rl[i][j] += a[i][k]*b[k][j]
            rl[i][j] %= 1000000007
    return rl



def x(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    temp = int(n-1)
    rl=[]

    while temp != 1:
        if temp % 2:
            rl.append(1)
        else:
            rl.append(0)
        temp = temp // 2

    rl.reverse()
    bs = [[1,1],[1,0]]
    tl = list(bs)

    for i in rl:
        tt = cal(tl,tl)
        if i:
            tl = cal(tt,bs)
        else:
            tl = tt

    return tl[0][0]

print(x(n))
            

