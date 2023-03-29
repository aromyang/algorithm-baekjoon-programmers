from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    sec = 0
    if start == k:
        return 0 
    while queue:
        for _ in range(len(queue)):
            cur_v = queue.popleft()
            dx = [-1, 1, cur_v]
            for d in range(3):
                next_v = cur_v + dx[d]
                if 0 <= next_v <= 100000 and not visited[next_v]:
                    if next_v == k:
                        return sec + 1
                    visited[next_v] = True
                    queue.append(next_v)
        sec += 1


print(bfs(n))
