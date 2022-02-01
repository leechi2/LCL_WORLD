import sys
input = sys.stdin.readline

n,c = map(int,input().split())

xloc = []
for _ in range(n):
    xloc.append(int(input()))
xloc.sort()

stt = 1
end = (xloc[n-1]- xloc[0])//(c-1)
res = 0

while stt <= end:
    mid = (stt+end)//2
    cnt = 0
    temp = int(xloc[0])
    for i in range(n):
        if xloc[i] - temp >= mid:
            cnt += 1   
            temp = int(xloc[i])
    if cnt < c -1:
        end = int(mid)-1
    else:
        stt = int(mid)+1
        res = mid

print(res)





