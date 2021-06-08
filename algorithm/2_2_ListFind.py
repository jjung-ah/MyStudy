def sol(L, x):
    ans = []
    c = 0
    same_count = 0
    for i in L:
        c += 1
        if i == x:
            same_count += 1
            ans.append(c-1)
    if same_count == 0:
        ans.append(-1)
    return ans