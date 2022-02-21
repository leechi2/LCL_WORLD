import sys
from collections import defaultdict

input= sys.stdin.readline
n = int(input())
a = str(input().rstrip())
list = [x for x in a]
sum = 0
for i in list:
    sum+=int(i)
print(sum)