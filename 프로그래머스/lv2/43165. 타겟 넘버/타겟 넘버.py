def solution(numbers, target):
    
    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                return 1
            return 0
        
        return dfs(depth + 1, total + numbers[depth]) + dfs(depth + 1, total - numbers[depth])
    
    return dfs(0, 0)
