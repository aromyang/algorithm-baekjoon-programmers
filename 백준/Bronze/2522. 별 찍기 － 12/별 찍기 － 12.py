n = int(input())
for i in range(1, n * 2):
    if i == n:
        print('*' * n)
    elif i > n:
        print(' ' * (i - n) + '*' * (n * 2 - i))
    else:
        print(' ' * (n - i) + '*' * i)
