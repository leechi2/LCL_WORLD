# 민수는 최근 숫자 세기 놀이에 푹 빠져있다. 민수는 숫자를 N진수로 세며,
# 9보다 큰 숫자는 한자리로 표현하기 위해 아래와 같이 바꾸어서 센다.
#
# - 10 ~ 35:  a~z (알파벳 소문자)
# - 36 ~ 61:  A~Z (알파벳 대문자)
#
# 민수가 N진수의 숫자를 start부터 end까지 센 결과를 counts라고 할 때, 민수가 잘 못 센 숫자의 개수를 반환하는 함수를 구현하시오.
#
# (단, 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)이다.)
#
#   | N | start | end | counts | return |
#   |---|-----|-------|---|--------|
#   | 14 | `'9'` | `'d'` | `['9', 'a', 'c', 'd', 'e']` | 3 |
#   | 62 | `'Z'` | `'12'` | `['Z', '10', '11', '12']` | 0 |

def solution(N, start, end, counts):
    answer = 0
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # 입력 받은거를 10진수로 바꿔주는 함수
    def int(x):
        xxxxxxx = 0
        test = list(x)
        temp = 0
        for i in range(len(test)):
            for p in range(len(base)):
                if test[i] == base[p]:
                    temp = p
            # list[i] 를 정수로 바꿔야됨
            xxxxxxx += temp * (N ** (len(test) - i - 1))
        return xxxxxxx

    # 다시 N 진수로 바꿔주는 함수
    def trans(x):
        result = []

        remain = 0
        quot = x
        while quot != 0:
            remain = quot % N
            result.append(base[remain])
            quot = quot // N

        return list(reversed(result))
    alpha = int(start)
    omega = int(end)
    count_list = []

    for i in range(omega - alpha + 1):
        temp = trans(alpha + i)
        temp = "".join(temp)
        count_list.append(temp)
    answer = len(counts)
    for abc in range(len(count_list)):
        if count_list[abc] == counts[abc]:
            answer -= 1







    return answer

print(solution(14, '9', 'd', ['9', 'a', 'c', 'd', 'e']))
print(solution(62, 'Z', '12', ['Z', '10', '11', '12']))
