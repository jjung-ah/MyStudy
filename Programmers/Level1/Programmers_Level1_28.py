# 정수 내림차순으로 배치하기  # 정렬알고리즘으로 다시

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



# 실행결과
# ('n: ', '11372')
# ('n_max: ', '8')
# ('answer: ', '8')
# ('n: ', '1132')
# ('n_max: ', '7')
# ('answer: ', '87')
# ('n: ', '112')
# ('n_max: ', '3')
# ('answer: ', '873')
# ('n: ', '11')
# ('n_max: ', '2')
# ('answer: ', '8732')
# ('n: ', '')
# ('n_max: ', '1')
# ('answer: ', '87321')

# ValueError: max() arg is an empty sequence


# 결과 만족한 함수
def solution(n):
    answer = ''
    str_n = str(n)
    n_list = list(str_n)
    n_list.sort()
    for i in n_list[::-1]:
        answer += i
    
    return int(answer)


# 실행결과
solution(118372)   # 873211
