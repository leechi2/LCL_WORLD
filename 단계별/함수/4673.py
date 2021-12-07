base_list = [x for x in range(10000)]

def d(a: int) -> int:
    nnnn = a//1000
    nnn = (a - nnnn*1000)//100
    nn = (a- nnnn*1000-nnn*100)//10
    n= a- nnnn*1000-nnn*100 - nn*10

    aa = a+nnnn+nnn+nn+n
    return aa

d_list = []

for i in range(10000):
    d_list.append(d(i))


for i in d_list:
    if i in base_list:
        base_list.remove(i)

for i in base_list:
    print(i)