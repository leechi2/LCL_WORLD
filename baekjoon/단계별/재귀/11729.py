import sys

input = sys.stdin.readline

def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n-1) + 1

rrrrr_list = []
for n in range(21):
    rrrrr_list.append([])
    if n == 0:
        rrrrr_list[0] = []
    elif n == 1:
        rrrrr_list[1] = [1,3]
    else:
        temp_hanoi_list = list(rrrrr_list[n-1])
        for i in range(len(rrrrr_list[n-1])):
            if rrrrr_list[n-1][i] == 3:
                temp_hanoi_list[i] = 2
            elif rrrrr_list[n-1][i] ==2:
                temp_hanoi_list[i] = 3
        temp_hanoi_list_2 = list(rrrrr_list[n-1])
        for i in range(len(rrrrr_list[n-1])):
            if rrrrr_list[n-1][i] == 1:
                temp_hanoi_list_2[i] = 2
            elif rrrrr_list[n-1][i] ==2:
                temp_hanoi_list_2[i] = 1

        rrrrr_list[n] = temp_hanoi_list + [1,3] + temp_hanoi_list_2


aaa = int(input())

print(hanoi(aaa))

result_list = rrrrr_list[aaa]
for i in range(len(result_list)):
    if i % 2 == 0:
        print(result_list[i], end=' ')
    else: 
        print(result_list[i])
