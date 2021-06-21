# Programmers_Level1_3.두 정수 사이의 합
def solution(a,b):
    
    list = [a,b]
    list.sort()    
    c = [i for i in range(list[0], list[1]+1)]    
    res = sum(c)
    
    return res