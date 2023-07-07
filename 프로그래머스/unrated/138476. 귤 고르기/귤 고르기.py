from collections import Counter, deque

def solution(k, tangerine):
    cnts = deque(Counter(tangerine).most_common())
    kind = 0
    t_sum = 0
    
    while cnts:
        _, cnt = cnts.popleft()
        kind += 1
        t_sum += cnt
        if t_sum >= k:
            break
    
    return kind