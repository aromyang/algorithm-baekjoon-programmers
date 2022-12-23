def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    boxes = len(score) // m
    for i in range(boxes):
        box = score[m * i: m * i + m]
        answer += min(box) * m

    return answer
