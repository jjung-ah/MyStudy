# Programmers48_스택/큐_프린터   # 다시 풀기

'''
def solution(priorities, location):
    answer = 0
    if priorities[location] == max(priorities):
        answer = 1
    else: 
        for i in priorities[priorities.index(max(priorities)):]:
            #print('i: ', i)
            if priorities[location] <= i:
                answer += 1
        for j in priorities[:location+1]:
            #print('j: ', j)
            if priorities[location] <= j:
                answer += 1
    
    return answer
'''
def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        print(cur)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# 실행코드 
priorities = [1, 1, 9, 1, 1, 1]
location = 0

solution(priorities, location)

'''
(0, 1)
[(1, 1), (2, 9), (3, 1), (4, 1), (5, 1), (0, 1)]
(1, 1)
[(2, 9), (3, 1), (4, 1), (5, 1), (0, 1), (1, 1)]
(2, 9)
(3, 1)
(4, 1)
(5, 1)
(0, 1)
5
'''