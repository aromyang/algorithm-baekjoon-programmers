from collections import deque

def solution(s):
    ss = deque(s)
    stack = []
    
    while ss:
        cur = ss.popleft()
        if stack and stack[-1] == cur:
            stack.pop()
        else:
            stack.append(cur)

    return 1 if not stack else 0