def solution(a, b):
    answer = 0
    for i, j in enumerate(a):
        answer += (j * b[i])
    
    return answer