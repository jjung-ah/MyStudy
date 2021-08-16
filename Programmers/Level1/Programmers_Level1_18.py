# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        print("number: ", number)
        cnt = 0
        for div in range(1, number+1):
            if number % div == 0:
                print("div: ", div)
                cnt += 1
        if cnt % 2 == 0:
            answer += number
            print("cnt: ", cnt)
            print("answer: ", answer)
        else:
            answer -= number
            print("answer: ", answer)
            
    return answer