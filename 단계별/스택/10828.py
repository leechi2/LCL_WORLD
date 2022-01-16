import sys
input = sys.stdin.readline
st = []
n = int(input())
def func(list):
    if list[0] == 'push':
        st.append(int(list[1]))
    if list[0] == 'pop':
        if len(st) ==0:
            print(-1)
        else:
            print(st.pop())
    if list[0] == 'size':
        print(len(st))
    if list[0] == 'empty':
        if len(st) ==0:
            print(1)
        else:
            print(0)
    if list[0] == 'top':
        if len(st) ==0:
            print(-1)
        else:
            print(st[-1])

for _ in range(n):
    temp = input().split()
    func(temp)