import heapq 

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    ans = 0
    heap = []
    
    for cur_enemy in enemy:
        if cur_enemy > n:
            if k > 0:
                if heap and -heap[0] > cur_enemy:
                    n += -heapq.heappop(heap)
                    heapq.heappush(heap, -cur_enemy)
                    n -= cur_enemy
                k -= 1
            else:
                break
        else:
            heapq.heappush(heap, -cur_enemy)
            n -= cur_enemy
        
        ans += 1
    
    return ans

