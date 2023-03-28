from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    grid = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    ans = 0

    for _ in range(k):
        xx, yy = map(int, input().split())
        grid[xx][yy] = 1


    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            cur_x, cur_y = queue.popleft()
            for d in range(4):
                next_x = cur_x + dx[d]
                next_y = cur_y + dy[d]
                if 0 <= next_x < m and 0 <= next_y < n:
                    if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))


    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1:
                bfs(i, j)
                ans += 1

    print(ans)
