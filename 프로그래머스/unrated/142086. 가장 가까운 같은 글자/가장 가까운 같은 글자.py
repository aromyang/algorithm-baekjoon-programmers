def solution(s):
    answer = []

    for i in range(len(s)):
        t = s[:i]
        idx = t.rfind(s[i])
        if idx == -1:
            answer.append(-1)
        else:
            answer.append(i-idx)
    
           
    return answer