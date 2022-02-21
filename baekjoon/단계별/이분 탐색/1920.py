import sys
input = sys.stdin.readline

n = int(input())
bs = list(map(int,input().split()))
bs.sort()

m = int(input())
dt = list(map(int,input().split()))


def fn(n):
    temp = len(bs)//2
    a = 0
    b = len(bs)-1
    while n != bs[temp]:
        if n > bs[temp]:
            a = int(temp + 1)
            temp = int((a + b)//2)
        else:
            b = int(temp -1) 
            temp = int((a + b)//2)
        if b - a < 2:
            if bs[a] == n:
                return 1
            elif bs[b] == n:
                return 1
            else:

                return 0
    return 1


for i in dt:
    print(fn(i))
