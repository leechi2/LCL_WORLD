#print 구문의 이해

#기분 출력
print('hello')
print("dasdas")
print("""dkdkdkdk""")
print()
print("a")

#seperater 옵션 사용
print('t','e','s','t', sep='')
print('t','e','s','t')
print('2021','07',sep='-')
print('이치이','com',sep='@')

#end옵션 사용
print('이창형',end='')
print(' 천재 ', end='')
print('코딩 공부')
print('aaaa')

#format 사용 [], {}, ()
print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('you', 'me'))
print('{a} and {b}'.format(a='you', b='me') )

# %s 는 문자, %d는 정수 %f는 실수
print("%s's favorite number is %d" %('이치이',7))

print("test1 : %5d, price : %4.7f ,d" %(2, 123798123809.3))
# %nd n은 자리수, %p.qf p는 정수 자리수 q는 소수자리수
print("test1 : {1: 5f}, price : {0:4.7f}".format(2, 123798123809.3))
print("test1 : {a: 5f}, price : {b:4.7f}".format(a=2, b=123798123809.3))

#print(''you'') --> 에러남
print("'you'")
print('\'you\'\n')
print('''\t\t\tyou''')