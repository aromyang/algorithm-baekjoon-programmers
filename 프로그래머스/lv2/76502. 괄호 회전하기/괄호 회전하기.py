from collections import deque

def solution(s):
    answer = 0
    stack = []
    pairs = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }
    
    for _ in range(len(s)):
        cur_deque = deque(s)
        valid = True
        while cur_deque:
            cur = cur_deque.popleft()
            if cur in pairs.values():
                stack.append(cur)
            elif not stack or stack.pop() != pairs[cur]:
                valid = False
                break
        answer = answer + 1 if valid and not stack else answer
        s = s[1:] + s[:1]
    
    return answer