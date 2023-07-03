def solution(s):
    stack = []
    
    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif stack and ss == ')':
            stack.pop()
        else:
            return False

    return not stack