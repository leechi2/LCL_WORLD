#section05-1
#파이썬 흐름제어(제어문)
#조건문 실습

print(type(True))
print(type(False))

#예1
if True:
    print('Yes')
# 예2
if False:
    print('No')
#예3
if False:
    print('No')
else:
    print('yess')

print()
#관계연산자
# >, >=, <, <=, ==< !=

a=10
b=0
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#참 거짓 종류
#참 : '내용', [내용], (내용), {내용}, 1
#거짓 : '', {}, [], (), 0
city = '' # city에 False 가 들어간다

if city:
    print('>>>>>>True')
else:
    print(">>>>>>False")

#논리 연산자
#and or not

a=100
b=60
c=15

print('and : ', a>b and b>c)
print("or  : ", a>b or c>b)
print('not : ', not a>b)
print()
print(not False)
print(not True)

#산술, 관계, 논리 연산자
#산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5+10 > 0 and not 7 + 3 ==10)
print()
score1 = 90
score2 = "A"

if score1 >= 90 and score2 == "A":
    print('합격')
else:
    print('탈락')

#다중 조건문
num = 0
if num>= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
else:
    print("num 등급 C", num)

#중첩 조건문
age = 17
height = 175
if age>= 20:
    if height >= 178:
        print('a지망 지원 가능')
    elif height >= 175:
        print('b지망 지원 가능')
    else:
        print('탈락')
else:
    print('20세 이상 지원 가능')

