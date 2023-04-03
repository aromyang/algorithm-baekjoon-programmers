from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    order, *num = map(str, input().split())
    num = int(num[0]) if num else None

    if order == 'push':
        queue.append(num)
    elif order == 'pop':
        print(-1) if not queue else print(queue.popleft())
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(1) if not queue else print(0)
    elif order == 'front':
        print(-1) if not queue else print(queue[0])
    elif order == 'back':
        print(-1) if not queue else print(queue[len(queue) - 1])
