import sys

input = sys.stdin.readline

n = int(input())
data_base = {}
for _ in range(n):
    a,b = input().rstrip().split()
    if int(a) not in data_base.keys():
        data_base.setdefault(int(a), [b])
    else:
        data_base[int(a)].append(b)

sorted_list = sorted(data_base.items())



for i in range(len(sorted_list)): # 총리스트
    for j in range(len(sorted_list[i][1])):
        print(sorted_list[i][0],sorted_list[i][1][j])