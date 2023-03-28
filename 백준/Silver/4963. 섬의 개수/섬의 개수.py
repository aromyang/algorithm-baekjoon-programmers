from collections import deque

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]


    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, 1, 1, -1, -1]

        while queue:
            cur_x, cur_y = queue.popleft()
            for d in range(8):
                next_x = cur_x + dx[d]
                next_y = cur_y + dy[d]
                if 0 <= next_x < h and 0 <= next_y < w:
                    if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))


    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
