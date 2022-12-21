def solution(dartResult):
    answer = 0
    before = 0
    temp = 0
    for i, d in enumerate(dartResult):
        if d == '1':
            if dartResult[i + 1] == '0':
                answer += temp
                before = temp
                temp = 10
                continue
        if d.isdigit():
            if d == '0' and dartResult[i - 1] == '1':
                continue
            else:
                answer += temp
                before = temp
                temp = int(d)
        elif d == 'S':
            temp **= 1
        elif d == 'D':
            temp **= 2
        elif d == 'T':
            temp **= 3
        elif d == '*':
            answer -= before
            answer += before * 2
            temp *= 2
        elif d == '#':
            temp *= -1

    return answer + temp
