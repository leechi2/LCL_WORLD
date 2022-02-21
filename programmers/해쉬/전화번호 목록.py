def solution(phone_book):
    hm = {}
    for i in phone_book:
        hm[i] = 1
    for i in phone_book:
        tmp = ""
        for j in i:
            tmp += j
            if tmp in hm and tmp != i:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))