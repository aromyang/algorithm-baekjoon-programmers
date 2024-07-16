from collections import deque

def bfs(maps, start, end):
    x_limit, y_limit = len(maps), len(maps[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([start])
    visited = [[False] * y_limit for _ in range(x_limit)]
    visited[start[0]][start[1]] = True
    distance = [[0] * y_limit for _ in range(x_limit)]
    
    while q:
        cur_x, cur_y = q.popleft()
        if (cur_x, cur_y) == end:
            return distance[cur_x][cur_y]
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < x_limit and 0 <= next_y < y_limit and not visited[next_x][next_y] and maps[next_x][next_y] != 'X':
                visited[next_x][next_y] = True
                distance[next_x][next_y] = distance[cur_x][cur_y] + 1
                q.append((next_x, next_y))
        
    return -1

def solution(maps):
    start, lever, exit = None, None, None
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'S':
                start = (x, y)
            elif maps[x][y] == 'L':
                lever = (x, y)
            elif maps[x][y] == 'E':
                exit = (x, y)
    
    distance_to_lever = bfs(maps, start, lever)
    if distance_to_lever == -1:
        return -1
    
    distance_to_exit = bfs(maps, lever, exit)
    if distance_to_exit == -1:
        return -1
    
    return distance_to_lever + distance_to_exit