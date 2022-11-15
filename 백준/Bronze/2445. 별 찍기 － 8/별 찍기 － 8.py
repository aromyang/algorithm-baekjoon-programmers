n = int(input())
for i in range(1, n * 2):
    if i * 2 <= n * 2:
        print('*' * i + ' ' * (n * 2 - i * 2) + '*' * i)
    else:
        print('*' * (n * 2 - i) + ' ' * (i * 2 - n * 2) + '*' * (n * 2 - i))
