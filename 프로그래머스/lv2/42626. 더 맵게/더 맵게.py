import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        
        if first >= K:
            return answer
            
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, (first + second * 2))
        answer += 1
    
    return answer if heapq.heappop(scoville) >= K else -1