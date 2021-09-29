# 정렬_H-Index

def solution(citations):
    citations.sort(reverse=True)
    #print(citations)
    answer = max(map(min, enumerate(citations, start=1)))

    return answer


# 실행 코드
solution([3, 0, 6, 1, 5])   # 3


'''
def solution(citations):
    answer = 0
    l = []
    for i in a:
        cnt = 0
        for j in a:
            if j >= i:
                cnt += 1
        if i >= cnt:
            l.append(i)
    answer = max(l)
    return int(answer)
'''