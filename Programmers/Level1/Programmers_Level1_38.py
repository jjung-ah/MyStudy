# 숫자 문자열과 영단어  

def solution(s):
    string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for idx, num in enumerate(string):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s
    return int(answer)


s1 = "one4seven56eightnine"
solution(s1)   # 1475689
