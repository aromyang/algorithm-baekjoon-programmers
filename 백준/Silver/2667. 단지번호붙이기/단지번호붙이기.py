from collections import deque

n = int(input())
visited = [[False] * n for _ in range(n)]
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))
houses = []


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    house = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        cur_x, cur_y = queue.popleft()
        house += 1

        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]

            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
    return house


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            houses.append(bfs(i, j))

houses.sort()
print(len(houses))
for h in houses:
    print(h)
