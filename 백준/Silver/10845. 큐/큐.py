import sys

input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    s = str(input().strip())
    if s == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        ss, x = map(str, s.split())
        queue.append(int(x))
