def solution(n):
    ans = 0
    
    while n > 0:
        if n & 1:
            ans += 1
        n //= 2

    return ans