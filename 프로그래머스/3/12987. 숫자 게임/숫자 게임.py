from collections import deque

def solution(A, B):
    answer = 0
    
    A = sorted(A, reverse=True)
    B = deque(sorted(B, reverse=True))

    for cur_a in A:
        b_max = B.popleft()
        if b_max > cur_a:
            answer += 1
        else:
            B.appendleft(b_max)
            B.pop()
    
    return answer