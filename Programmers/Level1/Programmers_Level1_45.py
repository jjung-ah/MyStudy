# Programmers45_완전 탐색_카펫

import math

cm = [(i, yellow//i) for i in range(1, int(math.sqrt(yellow))+1) if yellow%i==0]
print(cm)

for (w, h) in cm:
    #print(w, h)
    m = w+2
    n = h+2
    brown_cnt = 2*(m+n)-4
    if brown_cnt == brown:
        print(m, n)
        answer = [m, n]

#answer = [m, n]
print(sorted(answer, reverse=True))