import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

list1 = []

for i in range(n):
    temp = int(input())
    list1.append(temp)

list1.sort()

for i in range(len(list1)):
    print(list1[i])
