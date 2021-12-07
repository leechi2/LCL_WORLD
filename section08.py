# section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. -> 부모 디렉토리
# . -> 현재 디렉토리

# use1 (class)
from pkg.fibonacci import Fibonacci
Fibonacci.fib1(300)
print(Fibonacci.fib2(300))
print(Fibonacci().title)
print()
print()
print()
# use2 (class)
from pkg.fibonacci import * # *은 그 안에 class 싹다 가져오겠다
Fibonacci.fib1(300)
print(Fibonacci.fib2(300))
print(Fibonacci().title)
print()
print()
print()

# use3 (class)
from pkg.fibonacci import Fibonacci as fb
fb.fib1(300)
print(fb.fib2(300))
print(fb().title)
print()
print()
print()

# use4 (function)
import pkg.calculations as c # 얘는 안이 다 함수임

print(c.add(12, 4))
print(c.mul(12, 4))
print(c.div(11, 4))

# use5 (function)
from pkg.calculations import div as d # 필요한것만 가져오기
print(d(100,10))
print(d(50,1))
print(int(d(100,10)))

# use6
import pkg.prints as p
import builtins # 얘는 명시적으로 안해도 들어와있음
p.prt1()
p.prt2()
print(dir(builtins))

