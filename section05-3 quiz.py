# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for key in q1:
    if key == "가을":
        print('가을의 과일은 ',q1[key])
    else:
        print("x")
print(q1['봄'])
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k in q2:
    if q2[k]== '사과':
        print('사과있다')
        break
    else:
        print('...')
else:
    print('사과없다')
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score=5
if score > 80:
    print('A')
elif score > 60:
    print('B')
elif score > 40:
    print('C')
elif score > 20:
    print('D')
else:
    print("E")
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a=[12,6,18,99,9999]
max=0
for v in a:
    if v >= max:
        max = v


print(max)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
q5='2917232'
ll=list(q5)
print(ll)
print(ll[-1])
if int(ll[-1]) % 2 == 1:
    print("남자")
elif int(ll[-1]) % 2 == 0:
    print("여자")
else:
    print("외계인")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for v in q3:
    if v != '병':
        print(v)

for v in q3:
    if v == '병':
        continue
    else:
        print(v)
lc1 = [x for x in q3 if x != '정']
print(lc1)
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for v in range(1,101,2):
    print(v, end=", ")
lc2 = [x for x in range(1,101) if x % 2 == 1 ]
print(lc2)
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]
print()
for v in q8:
    if len(v) >= 5:
        print(v, end=" ")
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q5:
    if v.islower():
        print(v, end=' ')
print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for v in q6:
    if v.islower():
        print(v.upper(), end=" ")
    elif v.isupper():
        print(v.lower(), end=" ")
    else:
        print('bug', end=" ")
print()

#리스트 컴프리헨션
numbers=[]
for v in range(1,101):
    numbers.append(v)
print('numbers1 : ', numbers)

numbers2=[x for x in range(1,101) ]
print('numbers2 : ', numbers)