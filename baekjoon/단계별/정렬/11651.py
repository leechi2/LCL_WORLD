import sys

input = sys.stdin.readline

n = int(input())


dict1 = {}
for i in range(n):

    a,b = map(int, input().split())
    if b not in dict1.keys():
        dict1.setdefault(b,[a])
    else:
        dict1[b].append(a)

sorted_list = sorted(dict1.items())
print(sorted_list)
for i in range(len(sorted(dict1.keys()))):
    if len(sorted_list) == 1:
        print(sorted_list[i][1][0], end=' ')
        print(sorted_list[i][0])
    else:
        temp = sorted(sorted_list[i][1])
        for j in temp:
            print(j, sorted_list[i][0])

