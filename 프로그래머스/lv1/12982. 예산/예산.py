def solution(d, budget):
    dd = sorted(list(d))
    answer = 0
    for i in dd:
        budget -= i
        if budget >= 0:
            answer += 1
    return answer