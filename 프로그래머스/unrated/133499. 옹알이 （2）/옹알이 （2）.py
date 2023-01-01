def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']

    for b in babbling:
        for c in can:
            if (c * 2) in b:
                break
            elif c in b:
                b = b.replace(c, '*')
        if len(b) == b.count('*'):
            answer += 1
    return answer
