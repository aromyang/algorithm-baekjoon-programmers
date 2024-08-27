from collections import deque

def solution(board):
    limit_x, limit_y = len(board), len(board[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    min_cost_board = [[[float('inf')] * 4 for _ in range(limit_y)] for _ in range(limit_x)]
    
    initial_x, initial_y, initial_direction, initial_cost = 0, 0, -1, 0
    queue = deque([(initial_x, initial_y, initial_direction, initial_cost)])
    
    while queue:
        cur_x, cur_y, prev_direction, prev_cost = queue.popleft()
        
        for cur_direction, (dx, dy) in enumerate(directions):
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < limit_x and 0 <= next_y < limit_y and board[next_x][next_y] == 0:
                if prev_direction == initial_direction or prev_direction == cur_direction:
                    cur_cost = prev_cost + 100
                else:
                    cur_cost = prev_cost + 600
                    
                if cur_cost < min_cost_board[next_x][next_y][cur_direction]:
                    min_cost_board[next_x][next_y][cur_direction] = cur_cost
                    queue.append((next_x, next_y, cur_direction, cur_cost))
    
    return min(min_cost_board[limit_x - 1][limit_y - 1])