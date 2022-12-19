def solution(a, b, n):
    answer = 0
    while n >= a:
        bottle = (n // a) * b
        n = bottle + (n % a)
        answer += bottle
    return answer
