def solution(record):
    nick = {}
    answer = []
    
    for r in record:
        cur = r.split()
        if cur[0] == 'Enter':
            answer.append([cur[1]] + ['님이 들어왔습니다.'])
            nick[cur[1]] = cur[2]
        elif cur[0] == 'Leave':
            answer.append([cur[1]] + ['님이 나갔습니다.'])
        elif cur[0] == 'Change':
            nick[cur[1]] = cur[2]
    
    return [nick[a[0]] + a[1] for a in answer]