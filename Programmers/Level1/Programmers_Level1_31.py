# 3진법 뒤집기 

def solution(n):
    answer = 0
    reverse_num = ''
    while n > 0:
        n, r = divmod(n, 3)
        #print(n, r)
        reverse_num += str(r)
    #print(reverse_num)
    for i in range(len(reverse_num)):
        #print(int(reverse_num[i])* (3**(len(reverse_num) - (i+1))))
        answer += int(reverse_num[i])* (3**(len(reverse_num) - (i+1)))

    return answer



# 실행 결과
# n (10진법) = 125
# n (3진법) = 11122
# 앞뒤 반전(3진법) = 22111
# 10진법으로 표현 = 229

solution(125)   # 229

