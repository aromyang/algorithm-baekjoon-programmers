import sys
    
def solution(maps):
    sys.setrecursionlimit(10000)
    ans = []
    x_limit, y_limit = len(maps), len(maps[0])
    visited = [[False] * y_limit for _ in range(x_limit)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(cur_x, cur_y, days):
        days += int(maps[cur_x][cur_y])
        
        visited[cur_x][cur_y] = True
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < x_limit and 0 <= next_y < y_limit:
                if maps[next_x][next_y] != 'X' and not visited[next_x][next_y]:
                    days = dfs(next_x, next_y, days)
        
        return days
    
    for x in range(x_limit):
        for y in range(y_limit):
            if maps[x][y] != 'X' and not visited[x][y]:
                ans.append(dfs(x, y, 0))

    ans.sort()
    
    return ans if ans else [-1]