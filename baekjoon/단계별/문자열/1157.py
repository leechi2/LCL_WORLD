import sys
from collections import defaultdict

input= sys.stdin.readline

txt = list(input())

listt = []
for i in range(26):
    listt.append(0)

for i in range(65,91):
    temp = chr(i)
    for j in txt:
        if j == temp:
            count = listt[i-65]
            count +=1
            listt[i-65] = count


for i in range(97,123):
    temp = chr(i)
    for j in txt:
        if j == temp:
            count = listt[i-97]
            count +=1
            listt[i-97] = count

maxx = max(listt)
count = 0
for i in listt:
    if i == maxx:
        count+=1

if count >= 2:
    print('?')
else:
    print(chr(65 + listt.index(max(listt))))