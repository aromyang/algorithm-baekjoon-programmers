import sys

input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    s = str(input().strip())
    if s == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        ss, x = map(str, s.split())
        stack.append(int(x))
