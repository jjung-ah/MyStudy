Programmers46_ 깊이/너비 우선 탐색(DFS/BFS)_타겟넘버

#numbers = [1, 1, 1, 1, 1]
#target = 3
# return 5

numbers = [1, 2, 3, 4, 5]
target = 3

pair_numbers = [(x, -x) for x in numbers]
print(pair_numbers)

from itertools import product

product_numbers = list(product(*pair_numbers))
print(product_numbers)
print(len(list(product(*pair_numbers))))

answer = 0
for i in product_numbers:
    if sum(i) == target:
        answer += 1
        print(i)
print(answer)