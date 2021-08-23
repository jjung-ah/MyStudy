# 하샤드 수 

def solution(x):
    answer = True
    num = 0
    for i in str(x):
        num += int(i)
    if x % num == 0:
        return answer
    else:
        return not answer