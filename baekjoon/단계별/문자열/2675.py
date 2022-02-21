import sys
from collections import defaultdict

input= sys.stdin.readline

case= int(input())
for i in range(case):
    n, text = input().split()
    

    for j in text:
        for k in range(int(n)):
            print(j,end='')
    print()