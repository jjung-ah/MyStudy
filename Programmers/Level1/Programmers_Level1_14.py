from itertools import combinations

def prime_number(x):   # 소수인지 판별하는 함수
    for i in range(2, x):   # 2부터 x-1 까지 모든 수를 확인하면서
        if x % i == 0:   # x가 나누어 떨어지는 수가 있다면 
            return False   # 소수가 아니다
    return True


def solution(nums):
    answer = 0
    nums_combi = list(combinations(nums, 3))
    
    for i in nums_combi:
        nums_sum = sum(i)
        #print(nums_sum)
        if prime_number(nums_sum) is True:
            answer += 1

    return answer