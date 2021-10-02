# 해시_베스트앨범

def solution(genres, plays):
    #answer = []
    
    gen_total = {}
    for i in range(len(plays)):
        gen_total[genres[i]] = gen_total.get(genres[i], 0) + plays[i]
    #print(gen_total)


    gen_play = {}
    for i in range(len(plays)):
        gen_play[genres[i]] = gen_play.get(genres[i], []) + [(i, plays[i])]
    #print(gen_play)


    gen_sort = sorted(gen_total.items(), key=lambda x:x[1], reverse=True)
    #print(gen_sort)


    answer = []
    for (gen, playtotal) in gen_sort:
        play_sort = sorted(gen_play[gen], key=lambda x:x[1], reverse=True)
        #print(play_sort)
        answer += [idx for (idx, num) in play_sort[:2]]
    print(answer)
    return answer


# 실행 코드
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)   # [4, 1, 3, 0]