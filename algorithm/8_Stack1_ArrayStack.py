class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
        

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty() :
                return False
            else:
                t = S.pop()

                if t != match[c]:
                    return False
    return S.isEmpty()