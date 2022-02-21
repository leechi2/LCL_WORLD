import sys
input = sys.stdin.readline 
n = int(input())

def jg(list):
    c1 = 0
    c2 = 0
    for i in range(len(list)):
        if list[i] == '(':
            c1+=1
        else:
            c2 +=1
        if c2 > c1:
            return False
    if c1 == c2:
        return True
    else:
        return False

for _ in range(n):
    temp = list(input().rstrip())
    if jg(temp) == True:
        print('YES')
    else:
        print('NO')
