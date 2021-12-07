# 문자열 s1, s2, s3가 주어졌을 때, 문자열 s3가 문자열 s1과 s2를 교차로 배치하여 만들어질 수 있는지 여부를 출력하라.
#
# 예시 입력1
#
# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 출력: True
#
# 예시 입력2
#
# 입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 출력: False

def solution(s1, s2, s3):
    s1, s2, s3 = list(s1), list(s2), list(s3)
    for i in s3:
        temp = [s1[0], s2[0]]
        if i ==

    return False

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
solution(s1, s2, s3)
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
solution(s1, s2, s3)

