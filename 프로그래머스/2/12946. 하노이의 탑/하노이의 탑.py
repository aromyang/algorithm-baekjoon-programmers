def solution(n):
    def move(n, start, mid, end, answer):
        if n == 1:
            answer.append([start, end])
            return
        move(n - 1, start, end, mid, answer)
        answer.append([start, end])
        move(n - 1, mid, start, end, answer)
    
    answer = []
    move(n, 1, 2, 3, answer)
    return answer