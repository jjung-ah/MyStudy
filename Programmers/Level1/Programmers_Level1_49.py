# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    factor = []
    n_quotient = []
    m_quotient = []
    for i in range(1, m+1):
        n_quo, n_remainder = divmod(n, i)
        m_quo, m_remainder = divmod(m, i)
        if n_remainder == 0 and m_remainder == 0:
            factor.append(i)
            n_quotient.append(n_quo)
            m_quotient.append(m_quo)
    #print(factor[-1])
    #print(n_quotient[-1])
    #print(m_quotient[-1])
    answer = [factor[-1], factor[-1]*n_quotient[-1]*m_quotient[-1]]
    return answer


# 실행 결과
n = 12
m = 16

solution(n, m)   # [4, 48]