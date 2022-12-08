def solution(a, b):
    if a == b:
        return a
    
    aa = min(a, b)
    bb = max(a, b)
    answer = 0
    
    for i in range(aa, bb + 1):
        answer += i
        
    return answer;