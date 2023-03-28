from collections import deque

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    grid[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = grid[cur_x][cur_y] + 1
                    if next_x == n - 1 and next_y == m - 1:
                        return print(grid[next_x][next_y])


bfs(0, 0)
