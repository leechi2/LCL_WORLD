#section-7-1
#파이썬 클래스 상세 이해
#self, 클래스, 인스턴스 변수
#선언
#class 클래스명:
#   함수~
#   함수~

# EX1
class UserInfo: #클래스 선언시 앞은 대문자가 일반적인 규칙
    def __init__(self, name): #__하면 여러 함수가 나온다
        self.name=name
        print("초기화", name) #init은 클래스 시작시에 해야되며 초기화 기능
    def user_info_p(self):
        print('name : ', self.name)

# user1= UserInfo() name을 안넣으줬으므로 오류
# 클래스와 인스턴스의 차이를 이해하자
# 클래스는 틀같은거임
# 거기에 뭘 넣어서 인스턴스(사례)를 만드는거임
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
user2= UserInfo('lee')
user2.user_info_p()
print(user2.name)
print()
user3 = UserInfo('cho')
user3.user_info_p()
print(user3.name)
print()

print(id(user2)) #인스턴스 변수
print(id(user3)) #인스턴스 변수
print(user2.__dict__)
print(user3.__dict__)

# EX2
# self 의 이해
class SelfTest:
    def function1():
        print('func1 called')
    def function2(self):
        print(id(self))
        print('func2 called')

self_test = SelfTest() #인스턴스 변수 선언
#self_test.function1() 인스턴스인데 입력값(self)가 없어서
SelfTest.function1()
self_test.function2()
print(id(self_test))
SelfTest.function2(self_test)
#self가 없으면 class 에서 직접 호출

#ex3
#클래스 변수, 인스턴스 변수

class WareHouse:
    #클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num+=1
    def __del__(self):
        WareHouse.stock_num-=1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')
print()
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) #자기 네임스페이스에는 없음, 하지만 안나오는게 아니고 나온다 클래스로 가서 찾음
print(user2.stock_num)
print(user3.stock_num)
del user1
print(user2.stock_num)
print(user3.stock_num)

