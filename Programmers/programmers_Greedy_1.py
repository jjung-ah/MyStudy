# 체육복_다시 해보기
def solution(n, lost, reserve):
    #answer = 0
    survive = []
    for i in reserve:
        pre = i - 1
        back = i + 1
        if pre in lost:
            survive.append(pre)
        elif back in lost:
            survive.append(back)

    answer = n - len(lost) + len(set(survive))
    return answer