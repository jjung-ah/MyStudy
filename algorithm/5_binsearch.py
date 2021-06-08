def binsearch(L, x, lower, upper):    
    if lower > upper :
        return -1
    
    mid = (lower + upper)//2
    if x == L[mid]:        
        return mid
    elif x < L[mid]:
        return binsearch(L, x, lower, mid + idx)
    else:
        return binsearch(L, x, mid - idx, upper)



L = [1, 3, 7, 8, 12, 15, 16, 21, 23, 28, 35, 36, 41, 45, 52, 59, 64, 72]
x = 35
lower = 0
upper = len(L) - 1
idx = -1


binsearch(L, x, lower, upper)