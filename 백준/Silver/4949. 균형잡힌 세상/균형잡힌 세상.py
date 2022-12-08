def sol(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                return 'no'
            else:
                stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                return 'no'
            else:
                stack.pop()
    return 'yes' if not stack else 'no'


while True:
    sss = input()
    if sss == '.':
        break
    else:
        print(sol(sss))
