def solution(n):
    start = int(n)
    answer = start + 1
    bn = format(n, 'b')

    while True:
        answer = format(answer, 'b')
        if str(bn).count('1') == str(answer).count('1'):
            return int(answer, 2)
        else:
            answer = int(answer, 2) + 1