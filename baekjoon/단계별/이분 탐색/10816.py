import sys
input = sys.stdin.readline

n = int(input())
bs = sorted(list(map(int,input().split())))
m = int(input())
dt = list(map(int,input().split()))

def fn(stt,end,a):
    if stt > end:
        return 0
    mid = (stt+end)//2

    if bs[mid] == a:
        return bs[stt:end+1].count(a)
    elif bs[mid] > a:
        return fn(stt,mid-1,a)
    else:
        return fn(mid+1,end,a)

ndic = {}
for i in bs:
    st = 0
    endd = n - 1

    if i not in ndic:
        ndic[i] = fn(st,endd,i)
print(' '.join(str(ndic[i]) if i in ndic else '0' for i in dt))



