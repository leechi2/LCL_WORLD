import sys
a,b,c = map(int,input().split())

def cal(a,b,c):
    if b == 1:
        return a % c
    else:
        if b % 2 ==0:
            temp = cal(a,b//2,c)
            return temp * temp % c
        else:
            temp = cal(a,b//2,c)
            return temp * temp * a % c
            
print(cal(a,b,c))