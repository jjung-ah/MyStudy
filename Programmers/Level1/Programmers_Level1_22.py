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
'''
a = []    # 빈 리스트 생성
 
for i in range(2):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(1):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
print(a)
'''
