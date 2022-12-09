def solution(absolutes, signs):    
    answer = 0
    for i, j in enumerate(list(absolutes)):
        if signs[i]:
            answer += j
        else:
            answer -= j
    return answer