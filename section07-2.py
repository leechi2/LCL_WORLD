# section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# ex1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 서브 클래스에서 슈퍼클래스의 모든 속성 메소드 사용 가능

class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self):
        return " Your Car name is %s " % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self):
        return " Your Car name is %s " % self.car_name
    def show(self):
        # print(super().show())
        return "Car info is %s, %s, %s" % (self.car_name, self.color, self.type)

car1 = BenzCar("모름", 'sedan', 'white')
print(car1.color) #슈퍼클래스
print(car1.type) #슈퍼클래스
print(car1.car_name) #슈퍼클래스
print(car1.show_model())
print(car1.show())
print(car1.__dict__)

# Method overriding
car2 = BenzCar("g70", "suv", 'Black') #슈퍼 에도 있는 show 해보기
print(car2.show()) #슈퍼에 있는 show를 안하고 서브에 있는게 실행됨

# 슈퍼 클래스 Method를 사용하고 싶다면
# 서브의 메소드 안에서 부모의 메소드가 실행되도록


# Inheritance Info 상속 정보
print(BmwCar.mro())
#[<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
# object > Car > BmwCar 로 상속된다
print(BenzCar.mro())

# ex2
# 다중 상속
class X():
    pass # 나중에 채울떄는 pass를 넣자
class Y():
    pass
class Z():
    pass
class A(X, Y):
    pass
class B(Y, Z):
    pass
class M(B, A, Z):
    pass
print(M.mro()) # 상속을 너무 많이하면 오히려 복잡해짐
print(A.mro())
