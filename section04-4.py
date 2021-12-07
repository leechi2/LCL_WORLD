#section04-4
#파이썬 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리 : 순서x, 중복x, 수정o, 삭제o
#key, value (json) -> mongoDB

#선언

a={'name' : 'kim', 'phone': '010-~', 'birth' : 930330}
# 중복이 안된다 -> name이 두개면 name을 뽑을때 어떤걸 춫력할지 모른다
b={0 : 'hello lcl', 1 : 'hello ch'}
c={'arr':[1,2,3,4,5]}
print(type(a))

#출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

#딕셔너리 추가
a['address']='seoul'
print(a)
a['rank']=(1,2,3)
a['rank2']=[1,2,3,4]
print(a)

#key, values, items

#print(a.keys()[]) # errer 발생
print('keys : ',list(a.keys()))
temp=list(a.keys())
print(temp[:]) # 형 변환을 해야 indexing 가능
print('values : ',a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print(1 in b) # key가 1 인게 b 안에 있나
print('name2' in a )

#집합(sets): 순서x, 중복x
a=set()
b=set([1,2,3,4])
c=set([1,4,5,6,6])
print(type(a))
print(c) #6은 안나오는걸 볼 수 있다
t = tuple(b)
print(t)
l = list(b)
print(l)
l.pop()
print(l)
print()
print()

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1.intersection(s2))#교집합
print(s1&s2)
print()
print(s1|s2) #\ shift 누르고, 합집합
print(s1.union(s2))
print()
print(s1-s2) #차집합
print(s1.difference(s2))
print(s2.difference(s1))
print()
#추가 & 제거
s3= set([7,8,9,10])
s3.add(18)
print(s3)
s3.add(7)#이미 7이 있어서 뵨화 없음
print(s3)
print((type(s3)))

