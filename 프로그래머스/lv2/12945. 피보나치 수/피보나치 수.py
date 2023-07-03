import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    def fibo(n, memo):
        if n <= 1:
            return n
        elif n not in memo:
            memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
        return memo[n]
    
    return fibo(n, {}) % 1234567