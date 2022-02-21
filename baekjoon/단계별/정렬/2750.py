import sys

input = sys.stdin.readline

n = int(input())

def qsort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list()
    pivot = data[0]

    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else: 
            right.append(data[index])
    return qsort(left) + [pivot] + qsort(right)

list1 = []

for i in range(n):
    temp = int(input())
    list1.append(temp)

result_list = qsort(list1)

for i in range(n+1):
    print(result_list[i])

