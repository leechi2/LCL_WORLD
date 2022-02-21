import sys
input = sys.stdin.readline

a = list(input().rstrip())

p = []
m = []
sign = True
num = True
temp = []
def plus(list,sign):
    if sign == True:
        p.append(''.join(i for i in list))
    else:
        m.append(''.join(i for i in list))

for i in a:

    if i == '-':
        plus(temp,sign)
        temp = []
        sign = False

    elif i == '+':
        plus(temp,sign)
        temp = []
    else:
        temp.append(i)
plus(temp,sign)
re = 0
for i in p:
    re += int(i)
for i in m:
    re -= int(i)
print(re)
