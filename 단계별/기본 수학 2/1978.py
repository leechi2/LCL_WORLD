import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
count = len(data)
for i in range(len(data)):
    p = data[i]
    if p == 1:
        count -=1
    for j in range(2,int(p**(1/2))+1):
        if p % j == 0:
            count -=1
            break

print(count)