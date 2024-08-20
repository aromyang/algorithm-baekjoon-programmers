from collections import defaultdict

def solution(places):
    less_than_manhattan = {}
    
    for x1 in range(5):
        for y1 in range(5):
            less_than_manhattan[(x1, y1)] = [
                (x1 + dx, y1+ dy)
                for dx in range(-2, 3)
                for dy in range(-2, 3)
                if 0 <= x1 + dx <= 4 and 0 <= y1 + dy <= 4 and abs(dx) + abs(dy) <= 2
            ]
            
            
    def is_remote_enough(place, cur_x, cur_y):
        for close_x, close_y in less_than_manhattan[(cur_x, cur_y)]:
            if (close_x != cur_x or close_y != cur_y) and place[close_x][close_y] == 'P':
                if not is_blocked_with_partition(place, cur_x, cur_y, close_x, close_y):
                    return False
        return True
    
    def is_blocked_with_partition(place, cur_x, cur_y, close_x, close_y):
        if abs(cur_x - close_x) + abs(cur_y - close_y) == 1:
            return False
        
        if cur_x == close_x:
            return 'X' in [place[cur_x][(cur_y + close_y) // 2]]
        
        if cur_y == close_y:
            return 'X' in [place[(cur_x + close_x) // 2][cur_y]]
            
        return place[cur_x][close_y] == 'X' and place[close_x][cur_y] == 'X'
            
    def is_all_remote_enough(place):
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    if not is_remote_enough(place, x, y):
                        return 0
        return 1
        
    return [is_all_remote_enough(place) for place in places]