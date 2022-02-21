import sys

input = sys.stdin.readline

data_base = [3,6,9,12,5,10, 8, 11, 13, 14,0]
def solve(n):
    if n < 16:
        if n in (3, 5):
            print((n//15)*3+1)
        if n in (6,8,10):
            print((n//15)*3+2)
        if n in (9,11,13):
            print((n//15)*3+3)
        if n in (12, 14):
            print((n//15)*3+4)
        if n == 15:
            print((n // 15) * 3)
        if n % 15 not in data_base:
            print(-1)
    else:
        temp = n % 5
        count = 0
        while temp % 3!=0:
            temp +=5
            count +=1
        print((n//5-count+temp//3))

solve(int(input()))