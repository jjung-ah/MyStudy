# infix notation
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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    opStack = ArrayStack()
    postfixList = []

    for c in expr:
        if c in prec:
            if c == '(':
                opStack.push(c)
            else:
                if opStack.isEmpty():
                    opStack.push(c)
                else:
                    while not opStack.isEmpty() and prec[opStack.peek()] >=  prec[c]:
                        postfixList.append(opStack.pop())
                        print('ans3: ', postfixList)
                        print('opStack3 : ', opStack.data)
                    opStack.push(c)
        elif c == '(':
            opStack.push(c)
            print('opStack1 : ', opStack.data)
        elif c == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
                print('ans2: ', postfixList)
                print('opStack2 : ', opStack.data)
            opStack.pop()
        elif c not in prec or c != ')':   # 
            postfixList.append(c)
            print('ans1: ', postfixList)
    
    #스택이 빌 때까지 pop
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    result = 0

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        else:
            pop1 = valStack.pop()
            pop2 = valStack.pop()
            if tocken == '*':
                result = pop2 * pop1
            elif tocken == '/':
                result = pop2 / pop1
            elif tocken == '+':
                result = pop2 + pop1
            elif tocken == '-':
                result = pop2 - pop1
            valStack.push(result)

    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val