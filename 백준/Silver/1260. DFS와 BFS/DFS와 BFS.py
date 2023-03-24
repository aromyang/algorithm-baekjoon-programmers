import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start_v, visited):
    visited = [False] * len(graph)
    queue = deque([start_v])
    visited[start_v] = True
    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=' ')
        for i in graph[cur_v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(graph, v, visiited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visiited[i]:
            dfs(graph, i, visiited)
    
    
n, m, v = map(int, input().split())
graph = [[] * n for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n+1)
dfs(graph, v, visited)
print()
bfs(graph, v, visited)