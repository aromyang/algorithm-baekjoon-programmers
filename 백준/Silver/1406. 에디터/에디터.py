from collections import deque
import sys

input = sys.stdin.readline

lefts = list(input().strip())
rights = deque()
m = int(input())
for _ in range(m):
    command = input().strip()
    if command == 'L' and lefts:
        rights.appendleft(lefts.pop())
    elif command == 'D' and rights:
        lefts.append(rights.popleft())
    elif command == 'B' and lefts:
        lefts.pop()
    elif len(command) > 1:
        _, s = command.split()
        lefts.append(s)

print(''.join(lefts) + ''.join(rights))
