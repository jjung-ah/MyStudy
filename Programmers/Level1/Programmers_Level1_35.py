# 소수 찾기   # 다시하기   

# Version_1   # 답은 나오지만 런타임에러
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



# Version_2   # 마찬가지로 답은 나오지만 런타임에러
def solution(n):   # 주어진 숫자보다 작은 수 중에 소수가 있는지 판별하는 함수
    answer = 0
    for x in range(2, n+1):   # 주어진 숫자보다 작은 수 중에 소수가 있는지 확인하는 루프
        b = 0
        for i in range(2, x):   # 2부터 x-1 까지 모든 수를 확인하면서
            if x % i == 0:   # x가 나누어 떨어지는 수가 있다면 
                b = 1   # 소수가 아니다
        if b == 0:   # 소수이면
            answer += 1   # 카운트 +1 

    return answer

# 실행 코드
