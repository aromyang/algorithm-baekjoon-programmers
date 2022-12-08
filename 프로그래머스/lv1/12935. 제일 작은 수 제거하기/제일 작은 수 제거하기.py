def solution(arr):
    l = list(arr)
    if len(l) == 1:
        return [-1]
    
    l.remove(min(l))

    return l