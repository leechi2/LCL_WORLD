import sys

input = sys.stdin.readline

def fibonacci(n):
    if n > 1:
        return fibonacci(n-2) + fibonacci(n-1)
    elif n == 1:
        return 1
    else:
        return 0

print(fibonacci(int(input())))