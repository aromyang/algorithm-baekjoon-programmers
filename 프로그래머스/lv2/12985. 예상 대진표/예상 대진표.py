from collections import deque

def solution(n,a,b):
    participants = deque([(x, x) for x in range(1, n + 1)])
    cnt = 1
    
    while len(participants) > 2:
        n = 1
        for i in range(len(participants) // 2):
            first, _ = participants.popleft()
            second, _ = participants.popleft()
            
            if {first, second} == {a, b}:
                return cnt
            else:
                if first in (a, b):
                    participants.append((first, n))
                else:
                    participants.append((second, n))
            n += 1
        cnt += 1
        
    return cnt