def solution(s):
    idx = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            answer += ' '
        else:
            if idx & 1:
                answer += str(s)[i].lower()
            else:
                answer += str(s)[i].upper()
            idx += 1
    return answer