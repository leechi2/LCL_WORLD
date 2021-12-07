#section04-2
# 문자열, 문자열연산, 슬라이싱

str1= "나는 남자다"
str2= 'lcl'
str3=''
str4 = str('ace')
print(len(str1), '\n', len(str2), '\n',len(str3), '\n',len(str4))

escape_str1 = "do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \tTab"
print(escape_str2)

#Raw string

raw_str1 = r'c:\progames\test\bin'
print(raw_str1)
raw_str2 =  r"\\a\\a"
print(raw_str2)

#멀티 라인
# \가 있어야 그 다음을 그대ㅑ로 인싱 없으면 엔터에서 구분
multi = \
""""
문자열 
멀티라인 
테스트
"""
print(multi)

#문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "viceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('z ' in str_o4)

#문자열 형 변환

print(str(77)+'a')
print(str(10.4))
print(type(str(10.4)))

a = 'nice man'
b = 'orange'
print(a.islower()) # islower 소문자니
print(a.endswith('z'))
print(a.capitalize())
print(a.replace('e','it'))
print(list(reversed(b)))

print(a[0:3])
print(a[0:4])
print(a[0:8])
print(a[0:len(a)])
print(len(a))
print(a[:])
print(b[0::2])# 마지막 만큼 스킾을 하면서
print(b[1:-2]) # -2면 -1이 제일 뒤고 그아ㅠ
print(b[::-1]) # 처음 끝 지정 안된 사태에서 -1로 스킾되니까
