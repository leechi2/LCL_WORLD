#section 04-3
#파이썬 데이터 타입(자료형)
#리스트 튜플
#리스트(순서o, 중복o, 수정o, 삭제o)

#선언 방법 들
a=[]
b=list()
c=[1,2,3,4]
d=[10,100,'pen','orange', 'banana']
e= [10,100,['pen','orange', 'banana']]

#인덱싱
print(d[3], d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][-2:-1])

print(c+d)
print(c*3)
print(str(c[0])+' hi')

#리스트 수정 삭제
c[0]=77
print(c)
c[1:2] = [100,1000,10000]
#c[1] 이 2 였는데 100, 1000, 10000 3개 삽입으로 바뀜
print(c)
c[1] = ['a','b','c']
print(c)
del c[1]
print(c)
del c[-1]
print(c)
print()
print()

print()


#리스트 함수
y=[5,2,4,1,3]
print(y)
y.append(6)
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2) #del = 그 위치 제가
# remove는 그 값을 지움
y.pop()
print(y)
ex=[88,77]
y.extend(ex) #원소가 들어감
print(y)
y.append(ex) #그대로 들어감
print(y)

#삭제 : del, remove, pop

#튜플 (순서o, 중복o, 수정x, 삭제x)

a=()
b=(1,)
c=(1,2,3,4)
d=(1,10,('a','b','c'))
# del c[2] 이거 해보면 지원 안한다고 나옴

print(c[2])
print(c[3])
print(d[2][2])
print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print()
print()
#튜플 함수
z=(5,2,1,3,4,1)
print(z)
print(3 in z)
print(z.index(5)) #5 가 어느 위치에 있나
print(z.count(1))



