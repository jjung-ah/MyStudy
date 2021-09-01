# 정수 내림차순으로 배치하기

def solution(n):
    answer = ''
    str_n = str(n)
    for i in range(len(str_n)):
        n_max = max(str_n)
        index = str_n.find(n_max)
        answer += n_max
        str_n = str_n.replace(n_max, '')
        print('n: ', str_n)
        print('n_max: ', n_max)
        print('answer: ', answer)
            
    return answer