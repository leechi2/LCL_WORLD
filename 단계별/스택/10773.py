import sys
input = sys.stdin.readline
n = int(input())

st = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        st.pop()
    else:
        st.append(temp)
print(sum(st))