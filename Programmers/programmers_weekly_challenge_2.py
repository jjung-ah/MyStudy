def solution(scores):
    answer = ''
    score = 0
    for i in range(len(scores)):
        my_score = []
        for j in range(len(scores)):
            #print(scores[j][i])
            my_score.append(scores[j][i])
        #print(scores[i][i])    
        #print(my_score)
        if scores[i][i] == max(my_score) or scores[i][i] == min(my_score):
            last_score = sum(my_score) - scores[i][i]
            score = last_score / (len(scores)-1)
            #print(score)
        else:
            last_score = sum(my_score)
            score = last_score / len(scores)
            #print(score)

        if score >= 90:
            answer += 'A'
        elif score >= 80:
            answer += 'B'
        elif score >= 70:
            answer += 'C'
        elif score >= 60:
            answer += 'D'
        elif score >= 50:
            answer += 'E'
        else:
            answer += 'F'

    return answer
