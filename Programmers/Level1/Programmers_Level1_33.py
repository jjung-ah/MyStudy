# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    if 'p' not in s and 'y' not in s:
        return True
    else:
        if lower(s).count('p') == lower(s).count('y'):
            return true
        else:
            return false