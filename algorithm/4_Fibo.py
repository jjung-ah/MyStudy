# 재귀적 방법
def Fibo(n):
    if n < 0:
        return -1    # 또는 None
    elif n==0 or n==1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)



# 반복적 방법
def fibo(n):
    c1, c2, c3 = 1, 1, 1
    if n < 0:
        return -1    # 또는 None
    else:
        for i in range(n-1):
            c1 = c2
            c2 = c3
            c3 = c1 + c2
        return c3