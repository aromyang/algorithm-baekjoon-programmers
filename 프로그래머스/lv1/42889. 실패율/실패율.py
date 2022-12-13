def solution(N, stages):
    stages.sort()
    dic = {}
    idx = 1
    while idx <= N:
        if not stages or stages[0] != idx:
            dic[idx] = 0
        elif stages[0] == N + 1:
            dic[N] = 0
            stages.clear()
        else:
            fail = stages.count(idx)
            dic[idx] = fail / len(stages)
            stages = stages[fail:]
        idx += 1
    return sorted(dic, key=lambda x: dic[x], reverse=True)
