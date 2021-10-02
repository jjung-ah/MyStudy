# Programmers44_완전 탐색_소수 찾기

# 소수인지 판별하는 함수
def is_prime(n):
    b = 0
    for i in range(2,n):
        if n%i == 0:
            b = 1
            return 0
    if b == 0:
        return n


numbers = "17"
#numbers = "011"

num = [x for x in numbers]
#print(num)


# itertools 라이브러리를 이용한 permutations 함수를 사용해 순열의 경우의 수를 찾는다. 
from itertools import permutations

# 모든 가능한 경우를 찾는 방법
permu_list = []
for i in range(1, len(num)+1):
    for permu in permutations(num, i):
        #print(permu)
        permu_list.append(''.join(permu))
print(set(permu_list))

# 위에서 작성한 소수인지 판별하는 함수를 사용하여 소수를 찾아냄
prime_list = []
for x in set(permu_list):
    if int(x) == 0 or int(x) == 1:
        pass
    else:
      prime = is_prime(int(x))
      if prime == 0:
          pass
      else:
          prime_list.append(prime)
print(list(set(prime_list)))