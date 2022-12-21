def solution(food):
    answer = ''
    for i in range(1, len(food)):
        cnt = food[i] // 2
        answer += (str(i) * cnt)

    answer += '0'
    answer += answer[::-1][1:]

    return answer
