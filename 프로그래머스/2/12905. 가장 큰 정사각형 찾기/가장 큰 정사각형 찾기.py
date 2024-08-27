def solution(board):
    rows, cols = len(board), len(board[0])
    square_sizes = [[0] * (cols) for _ in range(rows)]
    max_square_side = 0

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                if row == 0 or col == 0:
                    square_sizes[row][col] = 1
                else:
                    square_sizes[row][col] = min(
                        square_sizes[row - 1][col]
                        , square_sizes[row][col - 1]
                        , square_sizes[row - 1][col - 1]
                    ) + 1
                max_square_side = max(max_square_side, square_sizes[row][col])
        
    return max_square_side ** 2