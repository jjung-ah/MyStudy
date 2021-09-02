# 정수 제곱근 판별

def solution(n):
    answer = 0
    n_root = n**0.5
    #print(n_root)
    if float.is_integer(n_root) == True:   # float 객체의 값이 정수인지 여부를 확인
        answer = int((n_root + 1)**2)
    else:
        answer = -1

    return answer


# 실행 결과
# n = 121
solution(n)  # 144
