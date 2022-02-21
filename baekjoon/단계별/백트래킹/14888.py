import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
sign = list(map(int,input().split()))
global result_list

result_list = []

def dfs(n, num_list, sign):


    if len(num_list) == 0:
        result_list.append(n)

    def complex(n,x,y):
        if n == 0:
            return x + y

        elif n ==1:
            return x - y

        elif n == 2:
            return x * y

        else:
            temp = 0
            if x > 0:
                temp = x // y
            elif x == 0:
                temp = 0
            else:
                temp == 0 - int(abs(x) // y)
            return temp

    temp = []
    for i in range(4):
        if sign[i] != 0:
            temp.append(i)
    for i in temp:
        sign[i] -= 1
        new_n = complex(i,n,int(num_list[0]))
        new_list = num_list[1:]
        dfs(new_n,new_list,sign)
        sign[i]+=1


    return

dfs(num_list[0], num_list[1:],sign)
print(max(result_list))
print(min(result_list))