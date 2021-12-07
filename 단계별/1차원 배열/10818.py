import sys
from collections import defaultdict

input= sys.stdin.readline

x= int(input())
y = list(map(int,input().split()))
print(sorted(y)[0], sorted(y)[x-1])

