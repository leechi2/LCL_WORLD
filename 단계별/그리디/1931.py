import sys
input = sys.stdin.readline

n = int(input())

dt = []

for _ in range(n):
    dt.append(list(map(int,input().split())))

dt.sort(key = lambda x: (x[1],x[0]))
temp = [0,0]
count = 0
for i in dt:
    if i[0] >= temp[1]:
        count +=1
        temp = list(i)
    
print(count)
