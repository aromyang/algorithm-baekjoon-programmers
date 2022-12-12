def solution(s, n):
    al = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for ss in s:
        lower = ss.lower()
        if lower in al:
            idx = al.find(lower)
            found = idx + n if idx + n < len(al) else idx + n - len(al)
            aa = al[found]
            if ss.islower():
                answer += aa
            else:
                answer += aa.upper()
        else:
            answer += ' '
    return answer