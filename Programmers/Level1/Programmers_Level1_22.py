# 행렬의 덧셈  ## 다시

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        line = []
        for j in range(len(arr2)):
            num = arr1[i][j] + arr2[i][j]
            line.append(num)
        answer.append(line)
    return answer