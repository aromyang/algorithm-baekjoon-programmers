def solution(book_time):
    rooms = []
    book_time.sort()
    
    def add_10minutes(time):
        h, m = map(int, time.split(':'))
        m += 10
        h += m // 60
        m = m % 60
        
        return f"{h:02d}:{m:02d}"
    
    def calculate_time_diff(prev_end, cur_start):
        h1, m1 = map(int, prev_end.split(':'))
        h2, m2 = map(int, cur_start.split(':'))
        
        return (h2 * 60 + m2) - (h1 * 60 + m1)
                    
    for start, end in book_time:
        end = add_10minutes(end)
        target_room_idx = -1
        for idx, room in enumerate(rooms):
            prev_end = room[-1]
            min_time_diff = 60 * 24
            cur_time_diff = calculate_time_diff(prev_end, start)
            if cur_time_diff >= 0 and cur_time_diff <= min_time_diff:
                target_room_idx = idx
                
        if target_room_idx != -1:
            rooms[target_room_idx].append(end)
        else:
            rooms.append([end])
    
    return len(rooms)