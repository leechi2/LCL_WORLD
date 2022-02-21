import sys

input = sys.stdin.readline

n = int(input())

list1 = []
dict1 = {}
for i in range(n):

    a,b = map(int, input().split())
    if a not in dict1.keys():
        dict1.setdefault(a,[b])
    else:
        dict1[a].append(b)

sorted_list = sorted(dict1.items())

for i in range(len(sorted(dict1.keys()))):
    if len(sorted_list) == 1:
        print(sorted_list[i][0], end= ' ')
        print(sorted_list[i][1][0])
    else:
        temp = sorted(sorted_list[i][1])
        for j in temp:
            print(sorted_list[i][0],j )

