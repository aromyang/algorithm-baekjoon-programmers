import heapq

def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
        
    while n > 0 and works:
        max_work = heapq.heappop(works)
        if max_work + 1 != 0:
            heapq.heappush(works, max_work + 1)
        n -= 1
    
    answer = 0
    
    for work in works:
        answer += work ** 2
    
    return answer