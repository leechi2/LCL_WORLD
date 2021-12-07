import sys

input = sys.stdin.readline

def tri(n):
    if n > 1:
        return list(i*3 for i in tri(n-1)) + list(i + ' '*len(i) + i for i in tri(n-1)) + list(i*3 for i in tri(n-1))
    elif n == 1:
        return ['***', '* *','***']

a = int(input())
count = 0
while a != 1:
    a = a/ 3
    count +=1

for p in tri(count):
    print(p)
