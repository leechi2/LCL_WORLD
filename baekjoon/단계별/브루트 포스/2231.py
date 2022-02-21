import sys

input = sys.stdin.readline
n = int(input())
for i in range(n+1):
    temp = i
    temp_list = list(str(i))
    for p in temp_list:
        temp += int(p)
    if temp == n:
        print(i)
        break
    if i == n:
        print(0)