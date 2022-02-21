n,m = map(int, input().split())
a = list(map(int,input().split()))
max = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k] > max and a[i]+a[j]+a[k] <= m:
                max = a[i]+a[j]+a[k]
print(max)
