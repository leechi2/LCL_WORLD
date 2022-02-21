import sys

input = sys.stdin.readline

p = int(input())
for _ in range(p):
    k = int(input())
    n = int(input())
    list1 = []
    temp=[]
    for i in range(1,n+1):
        list1.append(i)
        temp.append(0)

    for j in range(k):
        for p in range(n):
            if p == 0:
                temp[0] = list1[0]
            else:
                temp[p] = sum(list1[0:p+1])

        for m in range(n):
            list1[m] = temp[m]
    print(list1[n-1])