import sys
from collections import defaultdict

input= sys.stdin.readline

x=int(input())
for i in range(x):
    num = 0
    score = 0
    case = str(input())
    y = list (case)
    for i in range(len(y)):
        if y[i] == 'O':
            num +=1
            score += num
        if y[i] == 'X':
            num = 0
    print(score)
