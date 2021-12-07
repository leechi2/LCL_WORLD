# 이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다.
# 이진탐색을 이용하여 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고,
# target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.
# 예시 입력1


def searchMatrix(matrix, target):
  def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
      return True
    if len(data) == 1 and search != data[0]:
      return False
    if len(data) == 0:
      return False

    medium = len(data) // 2
    if search == data[medium]:
      return True
    else:
      if search > data[medium]:
        return binary_search(data[medium + 1:], search)
      else:
        return binary_search(data[:medium], search)

  for i in range(len(matrix)):
    if target < matrix[i][-1]:
      print(binary_search(matrix[i], target))
      break
    elif target == matrix[i][-1]:
      return True

  # if target > matrix[-1][-1]:
  #   return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
searchMatrix(matrix,3)
# target = 3
# 출력: True
# 예시 입력2

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
searchMatrix(matrix,13)
# target = 13
# 출력: False

