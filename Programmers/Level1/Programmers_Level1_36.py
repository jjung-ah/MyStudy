# 문자열 다루기 기본   # 문자열의 길이가 4 또는 6인지, 그리고 숫자인지 문자인지 판별하는 함수

def solution(s):
    #answer = True
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False

    #return s.lstrip("-").isdigit()
    #return s.isnumeric()


# 실행 코드
solution("a234")   # false
solution("1234")   # true
