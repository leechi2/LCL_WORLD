import sys

input = sys.stdin.readline
prime_list = []
for p in range(2, 123456*2):
    temp = 0
    for i in range(2, int((p + 1) ** (1 / 2)) + 1):
        if p % i == 0:
            temp = 1
            break
    if temp == 0:
        prime_list.append(p)
n = int(input())
while True:
    count=0					
    if n == 0 :
            break
    for i in prime_list:			
        if n < i <=2*n:		
            count+=1		
    print(count)
    n = int(input())