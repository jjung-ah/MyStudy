# 소수 찾기 

def prime_number(x):   # 소수인지 판별하는 함수
    for i in range(2, x):   # 2부터 x-1 까지 모든 수를 확인하면서
        if x % i == 0:   # x가 나누어 떨어지는 수가 있다면 
            return False   # 소수가 아니다
    return True

def solution(n):
    #answer = 0
    answer = []
    for j in range(2, n):
        if prime_number(j) == True:
            answer.append(j)
    return len(answer)


# 실행 코드
solution(10)   # 4
solution(5)   # 3