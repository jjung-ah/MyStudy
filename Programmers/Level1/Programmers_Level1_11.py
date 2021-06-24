# Programmers_Level1_11.2016년
def solution(a,b):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    d = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    date = sum(d[0:a-1]) + b + 5 
    idx = date % 7
    ans = day[idx-1]   
    return ans