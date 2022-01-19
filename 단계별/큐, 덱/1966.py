import sys
from collections import deque
input = sys.stdin.readline
a = int(input())

for _ in range(a):
    qq= deque([])
    n,k = map(int,input().split())
    temp = list(map(int,input().split()))
    count = 0
    for i in range(n):
        qq.append([temp[i],i])
    while qq:
        if qq[0][0] == max(temp):
            if qq[0][1] == k:
                print(count+1)
                break

            else:
                qq.popleft()
                temp.remove(max(temp))
                count +=1
        else:
            qq.append(qq.popleft())
        



