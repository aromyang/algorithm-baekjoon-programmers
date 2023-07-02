import heapq

def solution(jobs):
    heapq.heapify(jobs)
    total = len(jobs)
    first_start, first_time = heapq.heappop(jobs)
    min_time_heap = []
    heapq.heappush(min_time_heap, [first_time, first_start])
    cnt = first_start
    ans = 0
    
    while min_time_heap or jobs:
        if min_time_heap:
            cur_time, cur_start = heapq.heappop(min_time_heap)
            ans += cnt - cur_start + cur_time
            cnt += cur_time
        elif jobs:
            next_start, next_time = heapq.heappop(jobs)
            cnt = next_start
            heapq.heappush(min_time_heap, [next_time, next_start])
            continue
        
        while jobs and jobs[0][0] <= cnt:
            next_start, next_time = heapq.heappop(jobs)
            heapq.heappush(min_time_heap, [next_time, next_start])
        
    
    return ans // total