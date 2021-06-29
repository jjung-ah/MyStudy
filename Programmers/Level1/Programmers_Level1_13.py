# 같은 숫자는 싫어 
def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    return answer