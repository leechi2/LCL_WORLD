import sys
input = sys.stdin.readline
n = int(input())
def fib(n):
    if n == 0:
        return [1,0]
    elif n == 1:
        return [0,1]
    elif n == 2:
        return [1,1]
    else:
        temp_list = [1,0]
        temp = 0
        for _ in range(n):
            temp = temp_list[1]
            temp_list[1] = temp_list[0]+ temp
            temp_list[0] = temp
        return temp_list
for _ in range(n):
    print(' '.join(map(str,fib(int(input())))))
