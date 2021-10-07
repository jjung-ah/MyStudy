# 스택/큐_기능개발


def solution(progresses, speeds):
    #answer = []
    def update_processes(progresses, speeds):
        date = 0
        while progresses[0] < 100:
            date += 1
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        return progresses, date


    def pop_progresses(progresses):
        cnt = 0
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses = progresses[1:]
                cnt += 1
                #print(progresses)
        return progresses, cnt



    #progresses, date = update_processes(progresses, speeds)
    #print(progresses, date)
    #progresses, cnt = pop_progresses(progresses)
    #print(progresses, cnt)

    answer = []
    for i in range(len(progresses)):
        if len(progresses) > 0:
            update_processes(progresses, speeds)
            progresses, cnt = pop_progresses(progresses)
            answer.append(cnt)

    #print(answer)
    return answer