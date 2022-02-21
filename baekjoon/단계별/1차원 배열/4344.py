import sys
from collections import defaultdict

input= sys.stdin.readline

x=int(input())
for q in range(x):
    y = list(map(int,input().split()))
    case = y.pop(0)
    mean = sum(y)/case
    count = 0
    for i in range(case):
        if y[i] > mean:
            count +=1
    asdasd = round(float(count)/float(case)*100,3)
    print('%0.3f' % asdasd, end='')
    print('%')