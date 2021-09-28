# 정렬_가장 큰 수    

# 결과는 나오나 시간 초과 코드 1
from itertools import permutations

def solution(numbers):
    permu_list = list(permutations(numbers, len(numbers)))
    #print(permu_list)
    num_list = []
    for permu in permu_list:
        num = ''
        for j in permu:
            num += str(j)
        num_list.append(num)
    #print(num_list)
    answer = max(num_list)
    return answer

# 결과는 나오나 시간 초과 코드 2
def solution(numbers):
    numbers_string = [str(x) for x in numbers]  # 이걸로 해도 시간초과
    #numbers_string = list(map(str, numbers))   # 이걸로 해도 시간초과
    numbers_permu_list = list(map(''.join, permutations(numbers_string, len(numbers))))
    # permutations(numbers_string, len(numbers))에서 permutations(numbers, len(numbers)) 그냥 number로 permutations하면 에러 발생
    # TypeError: sequence item 0: expected string, int found
    #print(numbers_permu_list)
    answer = max(numbers_permu_list)
    
    return answer



# 실행 코드
solution([3, 30, 34, 5, 9])   # '9534330'
solution([6, 10, 2])   # '6210'
