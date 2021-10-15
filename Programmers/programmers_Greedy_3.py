# Programmers_탐욕법(Greedy)_구명보트

def solution(people, limit):
    people.sort() # 몸무게 오름차순 정렬
    answer = 0
    right, left = len(people) - 1, 0 # 가장 무거운 사람과 가장 가벼운 사람을 가리킴
    while right > left:
        if people[right] + people[left] <= limit: # 몸무게 합이 제한 무게보다 작거나 같으면 
            right -= 1 
            left += 1
        else: # 제한 무게보다 크면
            right -= 1 
        answer += 1
            
    if left == right: # 한 명이 남은 것이므로 +1
        answer += 1
    return answer


# 실행 코드
#people = [70, 50, 80, 50]
people = [70, 80, 50]
limit = 100

solution(people, limit)   # 3