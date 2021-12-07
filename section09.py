# section09
# file read, write
# read : r
# write : 기존 파일 삭제 - w, 추가 - a
# .. : 상대 경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# File read
# ex1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# 사용후에는 반드시 닫아야됨 아니면 예외 발생 할 수 있음
f.close()
print(' \n \n \n \n ')


# ex2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
print(' \n \n \n \n ')
print(c)
print(' \n \n \n \n ')
# ex3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
print(' \n \n \n \n ')

# ex4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content)
    content = f.read()
    print('>>>>', content)
    # 처음 읽을때 커서가 끝까지 가서 다음에는 아무것도 안읽어옴
print(' \n \n \n \n ')

# ex5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() #첫줄을 읽는다
    # print(line)
    while line:
        print(line, end = "####") # line이 되고 엔터가 된다
        line = f.readline()
print(' \n \n \n \n ')

# ex6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() #line 들을 list 형태로 가지고있다
    print(contents) # 리스트 보며는 \n 엔터가 들어가있다
    for c in contents:
        print(c, end = ' **************** ')
print(' \n \n \n \n ')

# ex6
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
    print()
print('{:6.3}'.format(sum(score)/len(score)))

# File write

# ex1
with open('./resource/test.txt', 'w') as f:
    f.write('lclclclclclcl\n')
# ex2
with open('./resource/test.txt', 'a') as f:
    f.write('asasasasasssa\n')

# ex3
from random import randint # random int
with open('./resource/test1.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0,45)))
        f.write('\n')

# ex4
# writelines : 리스트를 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'lee\n']
    f.writelines(list)

# ex5
with open('./resource/test3.txt', 'w') as f:
    print('lcl', file=f)
    print('lcl', file=f) #얘는 줄을 알아서 바꾸네여