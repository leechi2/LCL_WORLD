import sys

input = sys.stdin.readline

n = int(input())

base_list = list(map(int, input().split()))
sorted_list = sorted(list(set(base_list)))

data_base = {sorted_list[i] : i for i in range(len(sorted_list))}

print(data_base)

for i in base_list:
    print(data_base[i], end=' ')