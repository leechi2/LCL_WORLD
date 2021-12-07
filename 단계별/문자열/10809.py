import sys
from collections import defaultdict

input= sys.stdin.readline

text = list(input().rstrip())
raw_data = []

for i in range(97,123):
    temp = chr(i)
    raw_data.append(temp)

for i in raw_data:
    if i in text:
        temp = text.index(i)
        print(temp,end=' ')
    else:
        print(-1, end=' ')