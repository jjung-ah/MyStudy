# Programmers_Level1_2.가운데 글자 가져오기
def solution(s):
    
    import math
    idx = math.ceil(len(s)/2)
    
    if len(s)%2 == 0 :
        return s[idx-1:idx+1]        
    
    else :
        return s[idx-1]