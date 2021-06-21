# Programmers_Level1_1.완주하지 못한 선수 
def solution(participant, completion):
    
    c = participant + completion
    
    for i in c:
        d = c.count(i)
        if d%2 == 1 :
            return i