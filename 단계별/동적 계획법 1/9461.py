import sys

n = int(input())


for _ in range(n):
    p = int(input())
    temp_list = [1,1,1]
    if p < 4:
        print(1)
    else:
        for i in range(4, p+1):
            temp1 = int(temp_list[1])
            temp2 = int(temp_list[2])
            temp_list[2] = int(temp_list[0]+ temp_list[1])
            temp_list[0] = temp1
            temp_list[1] = temp2
        print(temp_list[2])