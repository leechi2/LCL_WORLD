import sys

input = sys.stdin.readline

n = input().rstrip()
list1 = list(str(n))

for i in list1:
    i = int(i)
list1.sort()

num = 0 
digit = 1
for i in list1:
    
    num +=int(i)*digit
    digit *= 10
list1.reverse()

print(num)