# 콜라츠 추측

def solution(num):
    answer = 0
    while num != 1:
        if answer > 500:
            answer = -1
            break
            #print('num1: ', num)
            #print('cnt1: ', answer)
        elif num % 2 == 0:
            num /= 2
            answer += 1
            #print('num2: ', num)
            #print('cnt3: ', answer)
        elif num % 2 == 1:
            num = num*3 + 1
            answer += 1
            #print('num3: ', num)
            #print('cnt3: ', answer)
                            
    return answer


# 실행결과
solution(6)   # 8
solution(16)   # 4
solution(626331)   # -1
