def solution(brown, yellow):
    yellow_x = 0
    
    while yellow_x <= yellow // 2:
        yellow_x += 1
        if yellow % yellow_x != 0:
            continue
        
        yellow_y = yellow // yellow_x
        if yellow_x * 2 + yellow_y * 2 + 4 == brown:
            return [yellow_y + 2, yellow_x + 2]
    
    return []