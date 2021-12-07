#section05-2
#파이썬 흐름제어 (반복문)
#반복문 실습

#코딩의 핵심 -> 조건 해결 중요

#기본 반복문 : for, while

v1= 1
while v1 < 11:
    print('v1 is : ', v1)
    v1+=1
print()
for v2 in range(10):
    print('v2 is : ', v2)
print()
for v3 in range(1,10):
    print('v3 is : ', v3)
print()

# 1~100 합
cnt1=0
sum1=0
while cnt1 <= 100:
    sum1 +=cnt1
    cnt1 +=1
print('1', sum1)

b=0
for a in range(1,101):
    b=b+a
print('2',b)

print('3',sum(range(1,101)))

print('4',sum(range(1,101,2)))

#시퀀스(순서가 있는) 자료형 반복
#문자열, 리스트, 튜플, 집합, 사전

#iterable 한 함수 종류: range , reversed, enumerate, filter, map, zip

names = ['kim', 'park', 'cho', 'choi', 'yoo']

for name in names:
    print('my name is ', name)

word = 'dreams'

for s in word:
    print(s)
info = {
    'name' : 'kim',
    'age' : 29,
    'city' : "seoul"

}
for key in info:
    print(key)
print()
for key in info.values():
    print(key)
print()
for key in info.keys():
    print(key)
print()
for key, value in info.items():
    print(key, value)
print()

name = "KennRY"
for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break : 반복문 탈출
numbers = [12,3,4,7,10,24,17,2,33,15,34,36,38]
for num in numbers:
    if num == 33:
        print('found')
        break
    else:
        print('...')
print()
#for- else 구문
for num in numbers:
    if num == 99:
        print('found')
        break
    else:
        print('...')
else:
    print('can\'t found')
# continue

list1=['1', 2,5,True, 4.3, complex(4)]
for v in list1:
    if type(v)is float:
        continue
    print(v, '\'s type is',type(v) )

v='niceman'
print(v[::-1])
