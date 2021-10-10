Programmers_탐욕법(Greedy)_큰 수 만들기

def solution(number, k):
    answer = ''
    bigs = []

    for i, num in enumerate(number):
        while len(bigs) > 0 and k > 0 and bigs[-1] < num:
            print('bigs1: ', bigs)
            bigs.pop()
            print('bigs2: ', bigs)
            k -= 1
        if k == 0:
            bigs += number[i:]
            print('bigs3: ', bigs)
            break
        bigs.append(num)
    print('bigs4: ', bigs)

    if k > 0:
        bigs = bigs[:len(number)-k]
    answer = ''.join(bigs)

    return answer


# 실행 코드
number = "1231234"
k = 3
solution(number, k)