def solution(numbers, hand):
    phone = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             ['*', 0, '#']]
    left = [1, 4, 7]
    right = [3, 6, 9]

    now_l = [3, 0]
    now_r = [3, 2]

    answer = ''

    for i, n in enumerate(numbers):
        if n in left:
            now_l = [left.index(n), 0]
            answer += 'L'
        elif n in right:
            now_r = [right.index(n), 2]
            answer += 'R'
        else:
            for j, nn in enumerate(phone):
                if n in nn:
                    dis_l = abs(now_l[0] - j) + abs(now_l[1] - 1)
                    dis_r = abs(now_r[0] - j) + abs(now_r[1] - 1)
                    if dis_l == dis_r:
                        if hand == 'left':
                            now_l = [j, 1]
                            answer += 'L'
                            break
                        else:
                            now_r = [j, 1]
                            answer += 'R'
                            break
                    elif dis_l < dis_r:
                        now_l = [j, 1]
                        answer += 'L'
                        break
                    else:
                        now_r = [j, 1]
                        answer += 'R'
                        break
    return answer
