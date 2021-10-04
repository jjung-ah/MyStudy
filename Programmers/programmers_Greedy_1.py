# 체육복_다시 해보기  # 맞는데 런타임에러   # 다시 하기
def solution(n, lost, reserve):
    #answer = 0
    PE = [[i, 1] for i in range(1, n+1)]
    #print(PE)
    #print(PE[2][0])

    for i in range(n):
        if PE[i][0] in lost:
            PE[i][1] = 0
        elif PE[i][0] in reserve:
            PE[i][1] = 2
    #print(PE)


    for i in range(n):
        pre = i-1
        next = i+1
        if PE[i][1]==0 and PE[pre][1]==2:
            PE[i][1] = 1
            PE[pre][1] = 1
        elif PE[i][1]==0 and PE[next][1]==2:
            PE[i][1] = 1
            PE[next][1] = 1


    answer = 0
    for i in range(n):
        if PE[i][1] == 1 or PE[i][1] == 2:
            answer += 1

    #print(answer)
    return answer
