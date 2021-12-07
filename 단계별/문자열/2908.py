import sys
from collections import defaultdict

input= sys.stdin.readline

a, b = input().split()

a ,b = list(a), list(b)

a.reverse()
b.reverse()

a= int("".join(str(_) for _ in a))
b= int("".join(str(_) for _ in b))
print(max(a,b))