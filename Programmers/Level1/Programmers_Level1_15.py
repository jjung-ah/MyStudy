# 두 개 뽑아서 더하기 
from itertools import combinations

def solution(numbers):
    answer = []
    nums_combi = list(combinations(numbers, 2))
    for i in nums_combi:
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()
    #print(sum_list)
    return answer