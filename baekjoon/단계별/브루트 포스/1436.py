import sys

input = sys.stdin.readline

n = int(input())

count = 0
a = 665
result_num = 0
while count != n:
    temp_list = list(str(a))
    for i in range(len(temp_list)-2):
        if temp_list[i] == '6':
            if temp_list[i+1] == '6':
                if temp_list[i+2]=='6':
                    count+=1
                    result_num = int(a)
                    break
    a+=1

print(result_num)

