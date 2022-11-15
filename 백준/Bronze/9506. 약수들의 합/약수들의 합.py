while True:
    n = int(input())
    if n == -1:
        break
    answer = str(n) + ' = 1'
    num = 1
    for i in range(n-2):
        if n % (i + 2) == 0:
            num += (i + 2)
            answer += (' + ' + str(i+2))
    if num == n:
        print(answer)
    else:
        print('{} is NOT perfect.'.format(n))
