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

'''
def solution(arr1, arr2):
    #answer = []
    answer = [[0 for j in range(len(arr2))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        #line = []
        #print(arr1[i])
        for j in range(len(arr2)):
            #print(arr2[j])
            num = arr1[i][j] + arr2[i][j]
            answer[i][j] = num

    return answer
'''
