def solution(arr, divisor):
    l = sorted(list(arr))
    answer = []
    for i in l:
        if i % divisor == 0:
            answer.append(i)
    return answer if answer else [-1]