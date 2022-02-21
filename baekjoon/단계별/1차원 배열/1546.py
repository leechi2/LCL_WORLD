import sys
from collections import defaultdict

input= sys.stdin.readline
x=int(input())
y=list()
y = list(map(int, input().split()))
max = max(y)
print(sum(y)/max*100/x)