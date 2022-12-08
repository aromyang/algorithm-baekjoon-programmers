def solution(num):
    if num == 1:
        return 0
    
    answer = 0
    while num != 1:
        if answer >= 500:
            return -1
        elif num & 1:
            num = num * 3 + 1
        else:
            num //= 2
        answer += 1
    
    return answer