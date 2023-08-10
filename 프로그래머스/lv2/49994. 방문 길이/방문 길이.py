from collections import deque

def solution(dirs):
    dirs = deque(dirs)
    cur = (0, 0)
    visited = set()
    
    def move(cur_, to_go_, visited):
        if (cur_, to_go_) not in visited and (to_go_, cur_) not in visited:
            visited.add((cur_, to_go_))
        return to_go_
    
    while dirs:
        command = dirs.popleft()
        # print('command = ', command, ', visited = ', visited)
        if command == 'U' and cur[1] < 5:
            to_go = (cur[0], cur[1] + 1)
            cur = move(cur, to_go, visited)
        elif command == 'D' and cur[1] > -5:
            to_go = (cur[0], cur[1] - 1)
            cur = move(cur, to_go, visited)
        elif command == 'R' and cur[0] < 5:
            to_go = (cur[0] + 1, cur[1])
            cur = move(cur, to_go, visited)
        elif command == 'L' and cur[0] > -5:
            to_go = (cur[0] - 1, cur[1])
            cur = move(cur, to_go, visited)
    
    print(visited)
    return len(visited)