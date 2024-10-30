def can_solve_in_limit(diffs, times, limit, cur_level):
    n = len(diffs)
    time_total, time_prev = 0, 0
    for i in range(n):
        diff, time_cur = diffs[i], times[i]
        if diff <= cur_level:
            time_total += time_cur
        else:
            time_total += ((time_cur + time_prev) * (diff - cur_level)) + time_cur
        
        if time_total > limit:
            return False
        time_prev = time_cur
    return time_total <= limit

def solution(diffs, times, limit):
    min_level = 1
    max_level = max(diffs)
    
    while min_level < max_level:
        cur_level = (min_level + max_level) // 2
        if can_solve_in_limit(diffs, times, limit, cur_level):
            max_level = cur_level
        else:
            min_level = cur_level + 1
    
    return min_level