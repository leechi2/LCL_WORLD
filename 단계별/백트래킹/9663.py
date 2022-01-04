import sys
input = sys.stdin.readline

n = int(input())
num_list = []
count = 0
def dfs():
    if len(num_list) == n:
        global count
        count += 1
        # print(num_list)
        return
    
    for i in range(n):
        if len(num_list) == 0:
            num_list.append(i)
            dfs()
            num_list.pop()
        elif i not in num_list:
            for j in range(len(num_list)):
                if int(j+num_list[j]) == int(i+len(num_list)):
                    break
                elif int(j-num_list[j]) == int(len(num_list)-i):
                    break
                if j == len(num_list)-1:
                    num_list.append(i)
                    dfs()
                    num_list.pop()

dfs()
print(count)
