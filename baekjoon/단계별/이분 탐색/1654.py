import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dt = []
for _ in range(n):
    dt.append(int(input()))

stt= 1
end = max(dt)
res = 0
while stt <= end:
    temp = 0
    mid = (stt+end)//2
    for i in range(n):
        temp += dt[i]//mid
    if temp >= k:
        res = int(mid)
        stt = int(mid) + 1
    else:
        end = int(mid) - 1
print(res)



