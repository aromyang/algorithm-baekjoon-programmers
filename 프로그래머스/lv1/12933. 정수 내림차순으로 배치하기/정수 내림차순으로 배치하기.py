def solution(n):
    l = sorted(list(str(n)), reverse=True)
    return int(''.join(s for s in l))