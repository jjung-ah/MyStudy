# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    a = 0
    for i in range(n):
        a += x
        answer.append(a)
    return answer