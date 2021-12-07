import sys
from collections import defaultdict
from typing import Text

input= sys.stdin.readline


x=1
for i in range(3):
    x = x* int(input())
y = list(str(x))
cal = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(y)):
    cal[int(y[i])] +=1

for i in range(10):
    print(cal[i])