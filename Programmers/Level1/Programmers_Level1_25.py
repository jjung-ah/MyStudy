# 이상한문자 만들기

def solution(s):
    answer = ''
    s_list = s.split(' ')
    #print(s_list)
    for j in s_list:
        #print(j)
        for i in range(len(j)):
            #print(s[i])
            if i % 2 != 0:
                answer += j[i].lower()
            else:
                answer += j[i].upper()
        answer += ' '
    return answer[:-1]



# 실행 결과
s = "try hello world"
solution(s)
# TrY HeLlO WoRlD
