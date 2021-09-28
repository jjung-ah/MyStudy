# 숫자 문자열과 영단어  

def solution(s):
    string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for idx, num in enumerate(string):
        if num in s:
            print(num, idx)
            s = s.replace(num, str(idx))
            print(s)
        answer = s
    return int(answer)


s1 = "one4seven56eightnine"
solution(s1)   # 1475689

'''
('one', 1)
14seven56eightnine
('seven', 7)
14756eightnine
('eight', 8)
147568nine
('nine', 9)
1475689
1475689
'''
