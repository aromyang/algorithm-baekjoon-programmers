def solution(n, arr1, arr2):
    answer = []
    init = '0' * n
    for i in range(n):
        arr1[i] = (init + format(arr1[i], 'b'))[-n:]
        arr2[i] = (init + format(arr2[i], 'b'))[-n:]
        a = ''
        for j in range(n):
            if arr1[i][j] == arr2[i][j] == '0':
                a += ' '
            else:
                a += '#'
        answer.append(a)
    return answer
