def gk(list):
    return list[1]

def solution(genres, plays):
    dict = {}

    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [[[i,plays[i]]],plays[i]]
        else:
            dict[genres[i]][0].append([i,plays[i]])
            dict[genres[i]][1] += plays[i]
    print(dict)
    for i in dict.keys():
        dict[i][0].sort(key =gk, reverse = True )

    a = list(dict.values())
    a.sort(key = gk, reverse=True)
    print(a)
    answer = []
    for i in a:
        answer.append(i[0][0][0])
        if len(i[0]) > 1:
            answer.append(i[0][1][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic",  "classic", "classic", "pop"], [100,  100, 100, 2500]))
print(solution(["a",  "a", "a", "b", "b", "b", "b", "b", "b","c","c","c"], [100,  100, 100, 2500,500, 600, 150, 800, 2500,100,  100, 100]))