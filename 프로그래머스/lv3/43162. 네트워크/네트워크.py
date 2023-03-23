from collections import deque

def bfs(start, computers, visited):
    answer = 0
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now not in visited:
            answer += 1
            visited.append(now)
        for i in range(len(computers)):
            if i != now and computers[now][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    return answer

def solution(n, computers):
    answer = 0
    visited = []
    for i in range(n):
        answer += bfs(i, computers, visited)
    return answer
