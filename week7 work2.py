# 여러 개의 구간이 리스트 intervals로 주어졌을 때, 겹치는 구간을 모두 병합하여 출력하시오.
#
# 입력 예시1
#
# 입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 출력: [[1,6],[8,10],[15,18]]
# 설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.
#
# 입력 예시 2
#
# 입력: intervals = [[1,4],[4,5]]
# 출력: [[1,5]]
# 설명: 구간 [1,4]와 [4,5]는 겹치는 것으로 간주한다.

def solution(intervals):
    def qsort(data):
        if len(data) <= 1:
            return data

        left, right = list(), list()
        pivot = data[0]

        for index in range(1, len(data)):
            if int(pivot[0]) > int(data[index][0]):
                left.append(data[index])
            else:
                right.append(data[index])

        return qsort(left) + [pivot] + qsort(right)
    sort = qsort(intervals)

    def insert(list):
        result = []
        for i in range(len(list)):
            if result == []:
                result.append(list[i])

            if result[-1][1] >= list[i][0]:
                result[-1] = [result[-1][0],list[i][1]]
            else:
                result.append(list[i])
        return result
    print(insert(sort))


    return []

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution(intervals)
intervals = [[1,4],[4,5]]
solution(intervals)