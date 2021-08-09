def solution(scores):
    answer = ''
    for i in range(len(scores)):
        my_score = []
        for scorelist in scores:
            #print(scorelist[i])
            my_score.append(scorelist[i])
        print(my_score)

    return answer
