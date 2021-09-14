# 자릿수 더하기

def solution(n):
    answer = 0
    str_n = str(n)
    for i in str_n:
        answer += int(i)

    return answer


# 실행 결과
solution(123)   # 6 (= 1+2+3)
solution(987)   # 24 (= 9+8+7)