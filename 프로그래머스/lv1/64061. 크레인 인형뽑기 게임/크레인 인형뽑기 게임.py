def solution(board, moves):
    stack = []
    answer = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                stack.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer
