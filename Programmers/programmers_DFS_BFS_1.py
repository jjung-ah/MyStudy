# Programmers_깊이/너비 우선 탐색(DFS/BFS)_네트워크

def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0]*n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1
        
        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer



'''
import numpy as np 
answers = [1,2,3,4,5]
#answers = [1,3,2,4,2]

p1 = [1, 2, 3, 4, 5]*2000
p2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
p1 = p1[:len(answers)]
p2 = p2[:len(answers)]
p3 = p3[:len(answers)]
eq1 = list(np.equal(p1, answers)).count(True)
eq2 = list(np.equal(p2, answers)).count(True)
eq3 = list(np.equal(p3, answers)).count(True)
answer = [eq1, eq2, eq3]

print(answer)
best = []
for idx,p in enumerate(answer, start=1):
    if p == max(answer):
        best.append(idx)

print(sorted(best))
'''
