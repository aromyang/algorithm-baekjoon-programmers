def solution(n, left, right):
    answer = []
    while left <= right:
        cur_row, cur_col = divmod(left, n)
        if cur_col > cur_row:
            answer.append(cur_col + 1)
        else:
            answer.append(cur_row + 1)
        left += 1
    
    return answer
