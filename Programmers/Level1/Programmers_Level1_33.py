# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    if 'p' not in s and 'y' not in s:
        return True
    else:
        if s.lower().count('p') == s.lower().count('y'):
            return True
        else:
            return False
       
    
# 실행결과
solution("pPoooyY")   # True
solution("Pyy")   # False
