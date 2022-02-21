def solution(progresses, speeds):
    tmp = []
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i] == 0:
            tmp.append((100-progresses[i])//speeds[i])
        else:
            tmp.append((100-progresses[i])//speeds[i]+1)
    temp = 1
    max = int(tmp[0])
    answer = []
    print(tmp)
    for i in range(1,len(speeds)):
        if tmp[i] > max:
            answer.append(temp)
            temp = 1
            max = int(tmp[i])
        else:
            temp += 1
    answer.append(temp)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))