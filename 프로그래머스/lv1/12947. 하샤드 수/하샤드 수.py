def solution(x):
    s = 0
    for i in str(x):
        s += int(i)
    return x % s == 0