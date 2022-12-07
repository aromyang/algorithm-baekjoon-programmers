def solution(s):
    org = list(s)
    answer = 0

    cnt = 1
    start = org.pop(0)
    while len(org) > 1:
        now = org.pop(0)
        if now == start:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            answer += 1
            cnt = 1
            start = org.pop(0)

    return answer if cnt == 0 else answer + 1
