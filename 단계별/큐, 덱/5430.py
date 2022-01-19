from re import T
import sys
from collections import deque

n = int(input())
def gg(list1,num,que):
    temp = True
    for i in list1:
        if i =='R':
            if temp == True:
                temp = False
            else:
                temp =True
        else:
            if num > 0:
                if temp == True:
                    que.popleft()
                else:
                    que.pop()
                num -=1
            else:
                return print('error')
    if temp == False:
        que.reverse()
    return print('['+','.join(que)+']')

for _ in range(n):
    ft = list(input())
    len = int(input())
    ll = deque(input().rstrip()[1:-1].split(','))
    
    gg(ft,len,ll)