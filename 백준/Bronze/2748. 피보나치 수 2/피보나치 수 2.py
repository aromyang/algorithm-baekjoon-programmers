def fibo(n):
    l = [0, 1, 1]
    for i in range(3, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[-1]


print(fibo(int(input())))
