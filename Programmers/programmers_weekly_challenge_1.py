# 부족한 금액 계산하기 programmers_weekly_challenge_1
def solution(price, money, count):
    #answer = -1
    price_sum = 0
    for i in range(count):
        price_sum += price * (i+1)
    #print(price_sum)
    
    if money > price_sum:
        answer = 0
    else:
        answer = price_sum - money

    return answer


# solution(3, 20, 4)   # 결과 10
# solution(3, 40, 4)   # 결과 0
