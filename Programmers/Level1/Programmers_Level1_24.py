# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    min_num = min(arr)
    #print(min_num)
    arr.remove(min_num)
    answer = arr
    if len(answer) == 0:
        answer = [-1]
    #print(answer)
    
    return answer