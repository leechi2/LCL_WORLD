# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일 알려주고 문법 체크를 해준다 -> 문법적인 오류 빈도 감소

# SyntaxError : 잘못된 문법
# 따옴표 안닫았을때 "" o " x
# if 문 등의 끝에 : 안붙였을 경우

# NameError : 참조변수 없음
# a, b 만을 선언해놓고 c를 부를 경우 등

# ZeroDivisionError : 0으로 나누기 에러

# IndexError : 인덱스 범위 초과
# x = [ 1, 2, 3 ] 이래놓고 x[3]을 부를때

# KeyError
# dictionary에 없는 key를 부를경우
# 방지법 : print(dic.get("키")) 키가 없더라도 none으로 출력해준다

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) 없는 모듈을 사용

# ValueError : 참조 값이 없을 때
# x = [1, 2, 3] x.remove(4) -> 4는 없는데 4를 지우라고 함
#               x.index(4) -> 4가 없는데 찾으려고함

# FileNotFoundError
# f = open('test.txt', 'r') 없는 애를 열라고 한다

# TypeError
# Tuple + List 또는 int + str

# 예외가 많지만 항상 예외가 없을 것 이라고 가정 후 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실핼
# except : 에러명1
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# ex1
name = ['kim', 'lee', 'cho']
try:
    z = 'lee'
    x= name.index(z)
    print('{} Found it in name'.format(z,x+1))except ValueError:
    print('Not Found It')
else:
    print("else")
print()

# ex2
name = ['kim', 'lee', 'cho']
try:
    z = 'kim'
    x= name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found It')
else:
    print("else")
finally:
    print('finally')

# ex3
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print("Finalllllly")
print()

# ex4
name = ['kim', 'lee', 'cho']
try:
    z = 'kim'
    x= name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not Found It - value')
except IndexError:
    print('Not Found It - index')
except Exception: # 얘는 기타임 따라서 위에 밸류, 인덱스보다 위이면 안됨
    print('Not Found It')
else:
    print("else")
finally:
    print('finally')

# 예제 5
# 예외를 발생시킴 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'km'
    if a == 'kim':
        print('ok')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print("asdasdfasd")