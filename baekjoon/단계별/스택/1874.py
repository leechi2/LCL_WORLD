import sys
input = sys.stdin.readline
n = int(input())

st = []
rl = []
count = 1

for i in range(1,n+1):
    data = int(input())
    while data >= count:
        st.append(count)
        count+=1
        rl.append('+')
    if data == st[-1]:
        st.pop()
        rl.append('-')
    else:
        print('NO')
        break

print('\n'.join(rl))



