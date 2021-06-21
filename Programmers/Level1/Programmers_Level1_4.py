# Programmers_Level1_4.K번째 수
def solution(array, commands):
    
    res = []    
    for i in commands:
        a = array[i[0]-1:i[1]]
        a.sort()
        res.append(a[i[2]-1])
        
    return res