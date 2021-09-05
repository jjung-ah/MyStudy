# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = [0]*len(str(n))
    str_n = list(str(n))
    #print('n: ', list(str_n))
    for i in range(len(str_n)):
        #print('i: ', i)
        answer[len(str_n)-1-i] = int(str_n[i])
        
    return answer


# 실행 결과
n = 12345
solution(n)   # [5,4,3,2,1]