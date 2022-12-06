import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deque = deque()
for i in range(n):
    s = str(input().strip())
    if s == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif s == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif s == 'size':
        print(len(deque))
    elif s == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif s == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    else:
        ss, x = map(str, s.split())
        if ss == 'push_front':
            deque.appendleft(int(x))
        else:
            deque.append(int(x))
