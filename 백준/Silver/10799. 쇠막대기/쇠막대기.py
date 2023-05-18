laser = list(map(str, input()))
stack = []
cnt = 0
open = 0

for l in laser:
    if l == '(':
        stack.append('(')
        open += 1
    elif l == ')':
        if stack[-1] == '(':
            open -= 1
            cnt += open
        else:
            open -= 1
            cnt += 1
        stack.append(')')

print(cnt)
