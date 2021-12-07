t= int(input())
l=[]
a,b=0,0
for x in range(t):
    a,b=map(int,input().split())
    l.append([a,b])
for x in range(t):
    a=int(l[x][0])
    b=int(l[x][1])
    print(a+b)