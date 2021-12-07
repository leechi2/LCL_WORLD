# 두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.
#
# 문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
# 가능한 C 중에 가장 긴 문자열을 C로 한다.
# 위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
# 이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.
#
# 예시입력1

A = 'ababcde'
B = 'ababcde'
# 출력: 'ababcde'
# 예시입력2

A = 'ababababab'
B = 'abab'
# 출력: 'ab'
# 예시입력3

C = 'abababab'
D = 'abab'
# 출력: 'abab'
# 예시입력3

E = 'fast'
F = 'campus'
# 출력: ''
def gcdString(A, B):
    if len(A) < len(B):
        A, B = B, A
    C = A[len(B):]

    if A == B:
        return A
    else:
        if A[:len(B)]==B:
            return gcdString(B,C)
        else:
            return "_"
print(gcdString(A,B))
print(gcdString(C,D))
print(gcdString(E,F))
