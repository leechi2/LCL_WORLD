import sys
input = sys.stdin.readline
n = int(input())

list1 = list([0] * 10001)

for i in range(n):
    num = int(input())
    list1[num]+=1

for i in range(10001):
    if list1[i] !=0:
        for j in range(list1[i]):
            print(i)
