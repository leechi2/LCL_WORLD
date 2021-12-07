#section06
#파이썬 함수식 및 람다(lambda)

#함수 정의 방법
#def 함수명 (parameter):

#함수 선언 위치 중요
#ex1
def hello(world):
    print('hello ', world)

hello('dlcldl')
hello(777)

#ex2
def hello_return(world):
    val='hello '+str(world) #숫자가 들어올수도있으니 형변환
    return val
str1 = hello_return('asdsdfasdf')
print(str1)

#ex3 (다중 return)
def fun1(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1, y2, y3
val1, val2, val3 = fun1(7)
print(type(val1), val1, val2, val3)

#ex4 (다중 return 이자만 type 다르게 받기)
def fun1(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return (y1, y2, y3)
lt1 = fun1(7)
print(type(lt1 ), lt1 )

#ex5
# *args, *kwargs arguement, key word

def args_func(*args): #입력값이 몇개인지 모를때
    print(args)
    for t in args:
        print(t)
    for i,v in enumerate(args):
        print(i,v)


args_func('lee')
args_func('lee', 'chang hyung')

# kwargs
def kwargs_func(**kwargs):
    print(kwargs)
    print()
    print(type(kwargs))
    print()
    for i,v in kwargs.items():
        print(i,v, end=" ")
kwargs_func(name1='kim',name2='cho',name3='lee')
print()
#전체 혼합
# 앞에 두개는 무조건 넣어야됨
# 뒤에는 가변적으로 튜플, 딕셔너리 형태로 받음
def example_func(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
example_func(10,20)
example_func(10,20,'suning', 'T1')
example_func(10,20,'suning' , t1='faker', ig='the shy' )

#중첩 함수 (클로져)
def nested_func(num):
    def func_infunc(num):
        print(num)
    print("in func")
    func_infunc(num+10000)
nested_func(100)
## 나중에 클로져, 데코레이터 찾아보자

#ex6 함수에 설명쓰기
def fun2(x : int) -> list:
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return (y1, y2, y3)
print(fun2('str')) # 안되지는 않는다

#람다식 예제
#람다식 장점 : 메모리 절약, 가독성 향상, 코드 간결하게
#함수는 객체 생성 -> 리소스(메모리) 할당
#그러나 람다는 즉시 실행(heap 초기화) -> 메모리 초기화

#일반 함수 예시
def func2(num : int)->int:
    return num*10 #y=num#20 & return y 한줄로다가
var_func=func2
print(var_func)
#<function func2 at 0x000001D7DF93F280> -> 아직 쓰지 않았지만 이미 메모리 할당 된걸 볼 수 있다
print(func2(10)) #print(var_func(10))
print()

lambda_func1 = lambda x:x*10
print(lambda_func1(1))

def func_final(x,y,func):
    print(x*y*func(10))
func_final(1,2,lambda_func1)
func_final(1,2,lambda x: x*10)





