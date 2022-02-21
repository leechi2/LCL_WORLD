import sys
from collections import defaultdict

input= sys.stdin.readline

x= int(input())
p=x +1
q = x +1
a=0
b=0
n=0
while p != x:
    if n == 0:
        p = x
    
    n+=1
    a = p//10
    b = p%10
    q=a+b
    p= 10 * b + q%10

print(n)