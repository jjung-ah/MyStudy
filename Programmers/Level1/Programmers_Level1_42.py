# 해시_전화번호 목록

def solution(phone_book):
    answer = True
    phonebook = sorted(phone_book)
    for a, b in zip(phonebook, phonebook[1:]):
        if b.startswith(a):
            return False
    return answer



# 실행 코드
solution(["119", "97674223", "1195524421"])   # false
solution(["123","456","789"])   # true
solution(["12","123","1235","567","88"])   # false