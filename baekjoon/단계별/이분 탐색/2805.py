import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dt = list(map(int,input().split()))

stt = 1
end = max(dt)
res = 0
while stt <= end:
    mid = (stt+ end )//2
    temp = 0
    for i in dt:
        if i > mid:
            temp += (i - mid)
    if temp < k:
        end  = int(mid) -1 
    else:
        res = int(mid) 
        stt = int(mid) + 1
print(res)