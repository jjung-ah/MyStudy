# postfix notation
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(expr):
    S = ArrayStack()
    answer = ''
    
    for c in expr:
                # 연산자인 경우
        if c in prec:
            if c == '(':      #'('이면 스택에 push
                S.push(c)
            else:             #'('이 아니면
                if S.isEmpty():     #빈 스택인 경우 push
                    S.push(c)
                else:      #스택 안과 밖의 연산자 우선순위 비교후 밖에 낮으면 꺼내고 반복
                    while not S.isEmpty() and prec[S.peek()] >=  prec[c]:
                        answer += S.pop()
                        #print('ans3: ', answer)
                        #print('S3 : ', S.data)
                    S.push(c)    #우선순위가 밖이 높으면 push
        elif c == '(':
            S.push(c)
            print('S1 : ', S.data)
        elif c == ')':     #')'이면 '('가 나올때까지 pop하고 출력
            while S.peek() != '(':
                answer += S.pop()
                #print('ans2: ', answer)
                #print('S2 : ', S.data)
            S.pop()
                #피연산자인 경우
        elif c not in prec or c != ')':   # 
            answer += c
            #print('ans1: ', answer)
    
    #스택이 빌 때까지 pop
    while not S.isEmpty():
        answer += S.pop()

    return answer


''' 결과
ans1:  A
ans1:  A 
ans1:  A  
ans1:  A  B
ans1:  A  B 
ans1:  A  B  
ans1:  A  B  C
ans2:  A  B  C-
S2 :  ['(', '+', '(']
ans2:  A  B  C-+
S2 :  ['(']
ans1:  A  B  C-+ 
ans1:  A  B  C-+  
ans1:  A  B  C-+  D
A  B  C-+  D*
'''