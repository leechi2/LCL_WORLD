import sys

input = sys.stdin.readline

m,n = map(int,input().split())

line = []
data_base = []
for _ in range(50):
    data_base.append(line)

for i in range(m):
    data_base[i] = list(str(input().rstrip()))

def compare(list):
    count1 = 0
    count2 = 0
    list1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    list2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if list[i][j] != list1[j]:
                    count1+=1
                if list[i][j] != list2[j]:
                    count2+=1
            if i % 2 == 1:
                if list[i][j] != list2[j]:
                    count1+=1
                if list[i][j] != list1[j]:
                    count2+=1
    min_num = min(count1,count2)
    return min_num


result_num = 64
for i in range(m-8+1):
    for j in range(n-8+1):
        temp_data = [data_base[i][j:j+8],data_base[i+1][j:j+8],data_base[i+2][j:j+8],data_base[i+3][j:j+8],data_base[i+4][j:j+8],data_base[i+5][j:j+8],data_base[i+6][j:j+8],data_base[i+7][j:j+8]]
        result_num = min(compare(temp_data), result_num)

print(result_num)


