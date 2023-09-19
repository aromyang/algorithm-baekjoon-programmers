def solution(name, yearning, photo):
    answer = [0] * len(photo)
    scores = dict(zip(name, yearning))
        
    for i, p in enumerate(photo):
        for n in p:
            answer[i] = answer[i] + scores.get(n, 0)
        
    return answer