def solution(n):
    w = '수박'
    if n & 1:
        return (w * (n // 2 + 1))[:-1]
    else:
        return w * (n // 2)