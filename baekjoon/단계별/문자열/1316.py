import sys

input = sys.stdin.readline

n = int(input())
count = n
for _ in range(n):
    txt_list = list(input().rstrip())
    temp = txt_list[0]
    data_base = []
    data_base.append(temp)
    for i in range(1,len(txt_list)):
        if txt_list[i] != temp:
            if txt_list[i] not in data_base:
                data_base.append(txt_list[i])
                temp = txt_list[i]
            else:
                count -=1
                break


print(count)