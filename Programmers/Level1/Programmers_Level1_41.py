# 해시_위장

def solution(clothes):
    answer = 1
    dic = {}
    for value, key in clothes:
        print(value, key)
        if key in dic.keys():
            dic[key].append(value)
            #print(dic)
        else:
            dic[key] = [value]
            #print(dic)

    for value in dic.values():
        #print(value, len(value))
        answer *= (len(value)+1)
        #print(answer)
    return answer-1


# 실행 코드
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])   # 5
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])   # 3