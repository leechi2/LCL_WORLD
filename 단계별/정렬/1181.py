import sys

input = sys.stdin.readline

n = int(input())

data_base = {}
for _ in range(n):
    temp = str(input().rstrip())
    if len(list(temp)) not in data_base.keys():
        data_base.setdefault(len(list(temp)), [temp])
    else:
        if temp not in data_base[len(list(temp))]:
            data_base[len(list(temp))].append(temp)

sorted_list = sorted(data_base.items())



for i in range(len(sorted_list)): # 총리스트
    sorted_list[i][1].sort()
    for j in range(len(sorted_list[i][1])):
        print(sorted_list[i][1][j])
 
