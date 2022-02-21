def solution(clothes):
    dict = {}
    for i in clothes:
        if i[1] not in dict:
            dict[i[1]] = 1
        else: 
            dict[i[1]] += 1

    tmp = 1
    for i in dict.keys():

        tmp = tmp * (dict[i]+1)

    return tmp -1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))