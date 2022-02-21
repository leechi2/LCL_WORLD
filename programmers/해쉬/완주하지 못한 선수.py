from collections import Counter

def solution(participant, completion):
    tmp = 0
    dict = {}
    for i in participant:
        dict[hash(i)] = i
        tmp += hash(i)
    for i in completion:
        tmp -= hash(i)
    return dict[tmp]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))