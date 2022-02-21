import sys
input = sys.stdin.readline
temp = 1
n , k = map(int,input().split())

p = 1000000007
if n == 1:
    d,e,f = 1,1,1
else:
    for i in range(1,n+1):
        temp = temp * i % p
        if i == n-k:
            d = int(temp)
        if k == 0:
            e = 1
        elif i == k:
            e = int(temp)
        if i == n:
            f = int(temp)

def nn(a,b):
    if b == 1:
        return a % p
    if b % 2 == 0:
        return (nn(a,b//2) ** 2) % p
    else:
        return ((nn(a,b//2) ** 2) * a) % p

print( ((f % p) * (nn(d * e, p - 2) % p)) % p )
