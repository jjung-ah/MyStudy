# 이상한문자 만들기

def solution(s):
    answer = ''
    for i in range(len(s)):
        #print(s[i])
        if i % 2 != 0:
            answer += s[i].lower()
        else:
            answer += s[i].upper()
    return answer



# 실행 결과
s = "try hello world"
solution(s)
# TrY HeLlO WoRlD