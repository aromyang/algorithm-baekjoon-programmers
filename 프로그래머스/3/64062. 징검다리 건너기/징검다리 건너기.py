from collections import deque

def solution(stones, k):
    def can_go(mid):
        count = 0
        for stone in stones:
            if stone - mid < 0:
                count += 1
                if count >= k:
                    return False
            else:
                count = 0
        return True
    
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        if can_go(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right