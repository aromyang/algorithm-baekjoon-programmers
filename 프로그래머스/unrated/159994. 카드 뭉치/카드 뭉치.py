def solution(cards1, cards2, goal):
    check = len(goal)
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
            check -= 1
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
            check -= 1
        else:
            return 'No'
    return 'Yes' if check == 0 else 'No'
