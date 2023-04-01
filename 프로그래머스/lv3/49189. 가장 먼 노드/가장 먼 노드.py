from collections import deque


def solution(n, edge):
    tree = [[] for _ in range(n + 1)]
    for e in edge:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])

    queue = deque()
    queue.append((1, 0))
    visited = [False] * (n + 1)
    visited[1] = True
    ans = {}

    while queue:
        cur_node, cur_depth = queue.popleft()
        ans[cur_depth] = 1 + ans.get(cur_depth, 0)
        for next_node in tree[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, cur_depth + 1))

    return ans[max(ans.keys())]