def solution(m, n, board):
    board = [list(row) for row in board]
    board_x = len(board)
    board_y = len(board[0])
    removed_blocks = 0

    def mark_blocks_to_remove():
        nonlocal board, board_x, board_y
        blocks_to_remove = [[False] * board_y for _ in range(board_x)]
        
        for x in range(board_x - 1):
            for y in range(board_y - 1):
                cur_block = board[x][y]
                
                if cur_block is None:
                    continue
                
                if (board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]):
                    blocks_to_remove[x][y] = True
                    blocks_to_remove[x + 1][y] = True
                    blocks_to_remove[x][y + 1] = True
                    blocks_to_remove[x + 1][y + 1] = True
        
        return remove_blocks(blocks_to_remove)
        
    def remove_blocks(blocks_to_remove):
        nonlocal removed_blocks, board, board_x, board_y
        cur_removed_blocks = 0
                
        for x in range(board_x):
            for y in range(board_y - 1, -1, -1):
                if blocks_to_remove[x][y]:
                    cur_removed_blocks += 1
                    board[x][y] = None
                
        if cur_removed_blocks == 0:
            return removed_blocks
        else:
            removed_blocks += cur_removed_blocks
            drop_blocks()
            return mark_blocks_to_remove()

            
    def drop_blocks():
        nonlocal board, board_x, board_y
        
        for y in range(board_y):
            empty_row = board_x - 1
            for x in range(board_x - 1, -1, -1):
                if board[x][y] is not None:
                    board[empty_row][y] = board[x][y]
                    if empty_row != x:
                        board[x][y] = None
                    empty_row -= 1
                    
                
    return mark_blocks_to_remove()