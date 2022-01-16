import sys
input = sys.stdin.readline
que = []
n = int(input())
count = 0
for _ in range(n):
    list = input().split()

    if list[0] == 'push':
        que.append(int(list[1]))
    elif list[0] == 'pop':
        if len(que)-count ==0:
            print(-1)
        else:
            print(que[count])
            count +=1
    elif list[0] == 'size':
        print(len(que)- count)
    elif list[0] == 'empty':
        if len(que) - count ==0:
            print(1)
        else:
            print(0)
    elif list[0] == 'front':
        if len(que) - count ==0:
            print(-1)
        else:
            print(que[count])
    elif list[0] == 'back':
        if len(que) - count ==0:
            print(-1)
        else:
            print(que[-1])