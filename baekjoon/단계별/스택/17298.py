import sys
input = sys.stdin.readline
n = int(input())
rl = [-1]*n
dt = list(map(int,input().split()))
st = [0]

for i in range(1,n):
    while st and dt[st[-1]] < dt[i]:
        rl[st.pop()] = dt[i]
    st.append(i)




for i in rl:
    print(i, end= " ")
