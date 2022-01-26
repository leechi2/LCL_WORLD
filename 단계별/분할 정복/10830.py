import sys
input = sys.stdin.readline 

n,k = map(int,input().split())

dt = []

for _ in range(n):
    dt.append(list(map(int,input().split())))

def cal(a,b):
    rl = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rl[i][j] += a[i][k] * b[k][j]
            rl[i][j] %= 1000
    return rl

def div(ll,k):
    if k == 1:
        return ll
    else:
        temp = div(ll,k//2)
        if k % 2:
            return cal(cal(temp,temp),ll)
        else:
            return cal(temp,temp)
ra = div(dt,k)

for i in ra:
    # print(' '.join(map(str, ra[i])))
    for j in i:
        print(j,end=' ')
    print()
