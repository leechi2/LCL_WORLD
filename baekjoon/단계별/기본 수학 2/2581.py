import sys

input = sys.stdin.readline

a = int(input())
b = int(input())

prime_list = list(range(a,b+1))
for i in range(a,b+1):
    if i == 1:
        prime_list.remove(i)
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0:
            prime_list.remove(i)
            break
if prime_list == []:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))