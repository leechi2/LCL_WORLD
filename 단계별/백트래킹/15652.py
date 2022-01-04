import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num_list = []

def dfs(s):
    if len(num_list) == m :
        print(' '.join(map(str,num_list)))
        return
    
    for i in range(s,n+1):
        if len(num_list) < m:
            num_list.append(i)
            dfs(i)
            num_list.pop()

dfs(1)
