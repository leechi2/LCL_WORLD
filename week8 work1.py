def solution(N):
    answer = 3
    x= 2
    y =0
    if N==0:
        answer = 1
        return answer
    if N == 1:
        answer = 3
        return answer

    for i in range(N-1):
        temp = x//2
        x += 2*y
        y = temp
        answer += x

    return answer

print(solution(2))
print(solution(4))