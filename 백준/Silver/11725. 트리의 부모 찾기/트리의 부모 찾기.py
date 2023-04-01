import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
queue = deque([1])
ans = [0] * (n + 1)
visited = [False] * (n + 1)
while queue:
    cur_node = queue.popleft()
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            ans[next_node] = cur_node
            queue.append(next_node)

for i in range(2, n + 1):
    print(ans[i])
    