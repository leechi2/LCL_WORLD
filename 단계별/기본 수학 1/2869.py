import sys

input = sys.stdin.readline

a,b,v = map(int, input().split())


n= (v - a) // (a - b)


while n > -1:
    if v - n * (a - b) - a <= 0:
        print(n+1)
        break
    elif a < b:
        print('불능')
        break
    n+=1