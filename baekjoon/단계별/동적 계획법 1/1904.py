import sys
input = sys.stdin.readline

n = int(input())
templist = [1,2]
if n == 1:
    print(templist[0])
elif n ==2:
    print(templist[1])
else:
    for i in range(3, n+1):
        temp = templist[1]
        templist[1] = int(templist[0] + templist[1] ) % 15746
        templist[0] = temp

    print(templist[1])





