# section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성
import random
import time

words = [] # 영어 단어 리스트
n=1 #게임 시도 횟수
cor_cnt = 0 # 정답 수
with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
    # print(words) # 단어 리스트 확인

input("Ready? press enter!")
start = time.time()

while n <= 5:

    random.shuffle(words)
    q = random.choice(words)
    print()
    print('Question # {}'.format(n))
    print(q) # 문제 출력

    x= input() # 타이핑 입력
    print()
    if str(q).strip() == str(x).strip():
        print("Pass")
        cor_cnt+=1
    else:
        print("Wrong")

    n+=1
end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >=3:
    print("합격")
else:
    print("탈락")

print("게임 시간 : ", et, "s", "정답 갯수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass