import sys
from collections import defaultdict

input= sys.stdin.readline

y=list()
for i in range(10):
    y.append(int(input())%42)
num=1
for i in range(10):
    for j in range(i+1,10):
        if y[i] == y[j]:
            break
        if j == 9:
            num+=1

print(num)