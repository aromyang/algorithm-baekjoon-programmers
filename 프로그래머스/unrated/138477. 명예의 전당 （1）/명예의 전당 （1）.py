def solution(k, score):
    rank = []
    answer = []
    for s in score:
        if len(rank) < k:
            rank.append(s)
            rank.sort(reverse=True)
        elif len(rank) >= k and s > rank[-1]:
            rank.pop()
            rank.append(s)
            rank.sort(reverse=True)
        answer.append(rank[-1])
    return answer