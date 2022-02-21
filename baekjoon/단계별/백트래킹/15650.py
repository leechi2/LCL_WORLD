import sys
input = sys.stdin.readline
n,m = map(int, input().split())


num_list = []

def dfs(s):
    if len(num_list) == m:
        print(' '.join(map(str,num_list)) )
        return
    for i in range(s,n+1):
        if i not in num_list:
            num_list.append(i)
            dfs(i+1)
            num_list.pop()

dfs(1)