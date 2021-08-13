# 핸드폰 번호 가리기 
def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer += i.replace(i, '*')
    answer += phone_number[-4:]
    #print(answer)
    return answer