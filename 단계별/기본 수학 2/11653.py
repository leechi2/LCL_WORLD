import sys

input = sys.stdin.readline

a = int(input())
temp = int(a)
if a == 1:
 print()
else:
    for i in range(2, a+1):
        while temp % i ==0:
            print(i)
            temp = temp / i