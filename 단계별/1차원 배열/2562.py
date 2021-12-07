import sys
from collections import defaultdict

input= sys.stdin.readline


y = list()

for i in range(9):
    x= int(input())
    y.append(x)
num = 0
max = -1
for i in range(9):
    if y[i] > max:
        max = y[i]
        num = i+1
print(max)
print(num)